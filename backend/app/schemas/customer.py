
from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    name: str
    phone: str
    email: EmailStr | None = None
    memo: str | None = None
    tags: list[str] | None = None


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    id: str
    merchant_id: str

    class Config:
        from_attributes = True


class CustomerList(BaseModel):
    items: list[CustomerResponse]
    total: int
    skip: int
    limit: int
