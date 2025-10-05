import logging
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks, Request
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, EmailStr, field_validator, Field
from sqlalchemy.future import select
from models.user import User
from services.database import get_db
from utils.password_hasher import hash_password, verify_password
from utils.jwt_handler import create_verification_token, create_access_token, verify_token_and_get_email
from utils.email_sender import send_email_async
import re
from datetime import timedelta

logger = logging.getLogger("app")

router = APIRouter()

class UserCreate(BaseModel):
    fullname: str = Field(..., min_length=4, description="Full name of the user")
    username: str = Field(..., min_length=4, max_length=20, description="Username for the user")
    email: EmailStr = Field(..., min_length=6, description="Email address of the user")
    password: str = Field(..., min_length=8, max_length=20, description="Password for the user")

    @field_validator('username')
    def username_validation(cls,v):
        if not re.match("^[a-zA-Z0-9_@]+$", v):
            raise ValueError("Username can only contain alphanumeric characters and underscores.")
        return v
    
    @field_validator('password')
    def password_validation(cls,v):
        if not re.match("^[A-Za-z0-9@#$%^&+=]+$", v):
            raise ValueError("Password can only contain alphanumeric characters and underscores.")
        return v

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="Email address of the user.")
    password: str = Field(..., min_length=8, description="Password for the user.")

class Token(BaseModel):
    token: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr = Field(..., description="Email address of the user.")

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8, description="New password for the user.")

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate, background_tasks: BackgroundTasks, request: Request, db: AsyncSession = Depends(get_db)):
    logger.info("Received registration request for email: %s", user_data.email)
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered.")
    
    hashed_password = hash_password(user_data.password)
    new_user = User(
        fullname=user_data.fullname, 
        username=user_data.username, 
        email=user_data.email, 
        password_hash=hashed_password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    logger.info("User registered successfully. User ID: %s", new_user.user_id)
    verification_token = create_verification_token(data={"sub": new_user.email})
    frontend_url = "http://localhost:4200/"
    verification_url = f"{frontend_url}verify-email?token={verification_token}"
    
    background_tasks.add_task(
        send_email_async,
        subject="Welcome to StudyGenie! Please Verify Your Email",
        email_to=new_user.email,
        template_name="register_mail.html",
        body_data={"username": new_user.username, "verification_url": verification_url}
    )
    return {"message": "User registered successfully. Please check your email to verify your account."}

@router.post("/verify-email", response_model=Token)
async def verify_email(token_data: Token, db: AsyncSession = Depends(get_db)):
    logger.info("Received email verification request.")
    try:
        email = verify_token_and_get_email(token_data.token)
    except HTTPException as e:
        logger.error("Token verification failed: %s", e.detail)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired verification token.")
    
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        logger.warning("Attempted verification for non-existent user: %s", email)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    access_token = create_access_token(data={"sub": user.email})
    logger.info("Email verified successfully for user: %s", user.email)
    return {"token": access_token}

@router.post("/login")
async def login_user(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_data.email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password.")
        
    access_token = create_access_token(data={"sub": user.email})
    return {
        "status": True,
        "message": "Login successful.",
        "data": {"token": access_token}
    }

@router.post("/forgot-password")
async def forgot_password(request: Request, email_request: ForgotPasswordRequest, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == email_request.email))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    reset_token = create_verification_token(data={"sub": user.email})
    frontend_url = "http://localhost:4200/"
    reset_url = f"{frontend_url}reset-password?token={reset_token}"
    
    background_tasks.add_task(
        send_email_async,
        subject="Password Reset Request",
        email_to=user.email,
        template_name="forgot_password_mail.html",
        body_data={"username": user.username, "reset_url": reset_url}
    )
    return {"message": "Password reset link has been sent to your email."}

@router.post("/reset-password")
async def reset_password(reset_request: ResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    try:
        email = verify_token_and_get_email(reset_request.token)
    except HTTPException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired reset token.")

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    user.password_hash = hash_password(reset_request.new_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return {"message": "Password has been successfully reset."}