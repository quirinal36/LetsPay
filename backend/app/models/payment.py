import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class Payment(Base, TimestampMixin):
    __tablename__ = "payments"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bill_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("bills.id"))
    merchant_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("merchants.id"))

    amount: Mapped[int] = mapped_column(Integer)
    method: Mapped[str | None] = mapped_column(String(50), nullable=True)
    pg_provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    pg_tid: Mapped[str | None] = mapped_column(String(100), nullable=True)

    card_company: Mapped[str | None] = mapped_column(String(50), nullable=True)
    card_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    installment: Mapped[int] = mapped_column(Integer, default=0)

    status: Mapped[str] = mapped_column(String(20), default="PENDING")
    paid_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancel_reason: Mapped[str | None] = mapped_column(Text, nullable=True)

    settlement_amount: Mapped[int | None] = mapped_column(Integer, nullable=True)
    settlement_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
