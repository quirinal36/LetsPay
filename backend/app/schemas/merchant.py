from pydantic import BaseModel, EmailStr


class MerchantBase(BaseModel):
    email: EmailStr
    business_name: str
    business_number: str
    representative_name: str
    phone: str


class MerchantCreate(MerchantBase):
    pass


class MerchantResponse(MerchantBase):
    id: str
    status: str

    class Config:
        from_attributes = True
