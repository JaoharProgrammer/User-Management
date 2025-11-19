from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(..., gt=0, lt=150)
    color: Optional[str] = Field(None, max_length=50)
    weight: float = Field(..., gt=0)
    height: float = Field(..., gt=0)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    weight: float
    height: float
    color: str  # Add if your model has this
    
    class Config:
        from_attributes = True