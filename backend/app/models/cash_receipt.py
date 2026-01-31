import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class CashReceipt(Base):
    __tablename__ = "cash_receipts"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    payment_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("payments.id"), nullable=True)
    merchant_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("merchants.id"))

    type: Mapped[str] = mapped_column(String(20))
    identity_type: Mapped[str | None] = mapped_column(String(20), nullable=True)
    identity_number: Mapped[str | None] = mapped_column(String(50), nullable=True)
    amount: Mapped[int] = mapped_column(Integer)

    approval_number: Mapped[str | None] = mapped_column(String(50), nullable=True)
    issued_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")
