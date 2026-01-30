from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class PaymentBase(BaseModel):
    bill_id: str
    amount: int


class PaymentResponse(BaseModel):
    id: str
    bill_id: str
    amount: int
    method: Optional[str] = None
    status: str
    paid_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PaymentList(BaseModel):
    items: List[PaymentResponse]
    total: int
    skip: int
    limit: int
