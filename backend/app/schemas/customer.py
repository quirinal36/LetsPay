from typing import Optional, List
from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    name: str
    phone: str
    email: Optional[EmailStr] = None
    memo: Optional[str] = None
    tags: Optional[List[str]] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    id: str
    merchant_id: str

    class Config:
        from_attributes = True


class CustomerList(BaseModel):
    items: List[CustomerResponse]
    total: int
    skip: int
    limit: int
