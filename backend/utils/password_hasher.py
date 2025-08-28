# backend/utils/password_hasher.py
from passlib.context import CryptContext

# Define the hashing context for passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a password for secure storage.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain-text password against a hashed one.
    """
    return pwd_context.verify(plain_password, hashed_password)