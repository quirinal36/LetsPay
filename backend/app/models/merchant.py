import uuid
from uuid import UUID

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class Merchant(Base, TimestampMixin):
    __tablename__ = "merchants"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    auth_user_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    business_name: Mapped[str] = mapped_column(String(255))
    business_number: Mapped[str] = mapped_column(String(20), unique=True)
    representative_name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    address: Mapped[str | None] = mapped_column(String(500), nullable=True)
    bank_code: Mapped[str | None] = mapped_column(String(10), nullable=True)
    bank_account: Mapped[str | None] = mapped_column(String(50), nullable=True)
    bank_holder: Mapped[str | None] = mapped_column(String(100), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="PENDING")
