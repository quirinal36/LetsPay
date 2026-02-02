from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class SignupRequest(BaseModel):
    email: EmailStr
    phone: str = Field(..., pattern=r"^01[0-9]-?[0-9]{3,4}-?[0-9]{4}$")
    business_name: str = Field(..., min_length=1, max_length=255)
    business_number: Optional[str] = Field(None, max_length=20)
    representative_name: Optional[str] = Field(None, max_length=100)
    supabase_user_id: Optional[UUID] = None


class SignupResponse(BaseModel):
    success: bool
    message: str
    merchant_id: str


class UserResponse(BaseModel):
    user_id: str
    email: Optional[str] = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class CheckEmailRequest(BaseModel):
    email: EmailStr


class CheckEmailResponse(BaseModel):
    available: bool
