from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class BillItemSchema(BaseModel):
    name: str
    quantity: int
    unit_price: int
    amount: int


class BillBase(BaseModel):
    customer_id: str
    amount: int
    title: str
    description: str | None = None
    items: list[BillItemSchema] | None = None
    tax_type: Literal["TAX", "TAX_FREE"] = "TAX"
    send_type: Literal["IMMEDIATE", "SCHEDULED", "RECURRING"]
    send_channel: Literal["ALIMTALK", "SMS", "BOTH"]
    scheduled_at: datetime | None = None
    message: str | None = None


class BillCreate(BillBase):
    pass


class BillResponse(BaseModel):
    id: str
    merchant_id: str
    customer_id: str
    bill_number: str
    amount: int
    title: str
    description: str | None = None
    tax_type: str
    send_type: str
    send_channel: str
    status: str
    sent_at: datetime | None = None
    paid_at: datetime | None = None

    class Config:
        from_attributes = True


class BillList(BaseModel):
    items: list[BillResponse]
    total: int
    skip: int
    limit: int
