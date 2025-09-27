from http.client import HTTPException
import os
from datetime import datetime, timedelta
from typing import Optional
from grpc import Status
from jose import JWTError, jwt
from dotenv import load_dotenv

load_dotenv()

# Load JWT settings from environment variables
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
VERIFICATION_TOKEN_EXPIRE_HOURS = int(os.getenv("VERIFICATION_TOKEN_EXPIRE_HOURS", 24))

# Ensure the JWT_SECRET_KEY is not None. This prevents the JWKError.
if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY not found. Please set it in your .env file.")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Creates a standard access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_verification_token(data: dict):
    """Creates a verification token with a longer expiration time."""
    expires_delta = timedelta(hours=VERIFICATION_TOKEN_EXPIRE_HOURS)
    return create_access_token(data, expires_delta=expires_delta)

def verify_token_and_get_email(token: str):
    """
    Decodes and validates a JWT token and returns the user's email.
    Raises HTTPException if the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise JWTError("Invalid token payload.")
        return email
    except JWTError:
        raise HTTPException(
            status_code=Status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token."
        )
