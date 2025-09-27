# backend/schemas/response_models.py
from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

# A generic type variable is used for dynamic data types in the response
T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    """
    A generic API response model for consistent output.
    
    Attributes:
        status (bool): Indicates if the request was successful.
        message (str): A human-readable message about the result.
        data (Optional[T]): The actual payload, which can be of any type.
    """
    status: bool
    message: str
    data: Optional[T] = None

class LoginSuccessData(BaseModel):
    """
    Data model for a successful login response.
    
    Attributes:
        token (str): The authentication token for the user.
    """
    token: str
