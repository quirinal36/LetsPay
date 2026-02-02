from uuid import UUID
from typing import Optional
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin
import uuid


class Merchant(Base, TimestampMixin):
    __tablename__ = "merchants"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    auth_user_id: Mapped[Optional[UUID]] = mapped_column(PGUUID(as_uuid=True), unique=True, nullable=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    business_name: Mapped[str] = mapped_column(String(255), default="")
    business_number: Mapped[str] = mapped_column(String(20), default="")
    representative_name: Mapped[str] = mapped_column(String(100), default="")
    phone: Mapped[str] = mapped_column(String(20), default="")
    address: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    bank_code: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    bank_account: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    bank_holder: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="PENDING")
