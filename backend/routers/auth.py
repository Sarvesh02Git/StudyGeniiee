# backend/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from services.database import get_db
from utils.password_hasher import hash_password, verify_password
from models.user import User
from sqlalchemy import select

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    """Registers a new user."""
    # Check if user already exists
    existing_user = await db.execute(select(User).where(User.email == user_data.email))
    if existing_user.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered.")
    
    # Hash the password and create a new user
    hashed_password = hash_password(user_data.password)
    new_user = User(username=user_data.username, email=user_data.email, password_hash=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return {"message": "User registered successfully."}

@router.post("/login")
async def login_user(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    """Logs in an existing user."""
    result = await db.execute(select(User).where(User.email == user_data.email))
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    
    # In a real app, you would generate and return a JWT token here.
    return {"message": "Login successful.", "user_id": user.user_id}