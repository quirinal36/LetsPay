from datetime import datetime

from pydantic import BaseModel


class PaymentBase(BaseModel):
    bill_id: str
    amount: int


class PaymentResponse(BaseModel):
    id: str
    bill_id: str
    amount: int
    method: str | None = None
    status: str
    paid_at: datetime | None = None

    class Config:
        from_attributes = True


class PaymentList(BaseModel):
    items: list[PaymentResponse]
    total: int
    skip: int
    limit: int
