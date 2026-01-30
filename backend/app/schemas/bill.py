from typing import Optional, List, Literal
from pydantic import BaseModel
from datetime import datetime


class BillItemSchema(BaseModel):
    name: str
    quantity: int
    unit_price: int
    amount: int


class BillBase(BaseModel):
    customer_id: str
    amount: int
    title: str
    description: Optional[str] = None
    items: Optional[List[BillItemSchema]] = None
    tax_type: Literal["TAX", "TAX_FREE"] = "TAX"
    send_type: Literal["IMMEDIATE", "SCHEDULED", "RECURRING"]
    send_channel: Literal["ALIMTALK", "SMS", "BOTH"]
    scheduled_at: Optional[datetime] = None
    message: Optional[str] = None


class BillCreate(BillBase):
    pass


class BillResponse(BaseModel):
    id: str
    merchant_id: str
    customer_id: str
    bill_number: str
    amount: int
    title: str
    description: Optional[str] = None
    tax_type: str
    send_type: str
    send_channel: str
    status: str
    sent_at: Optional[datetime] = None
    paid_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class BillList(BaseModel):
    items: List[BillResponse]
    total: int
    skip: int
    limit: int
