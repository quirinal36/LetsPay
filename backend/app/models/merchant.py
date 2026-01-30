from typing import Optional, List
from uuid import UUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin


class Merchant(Base, TimestampMixin):
    __tablename__ = "merchants"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    auth_user_id: Mapped[UUID] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    business_name: Mapped[str] = mapped_column(String(255))
    business_number: Mapped[str] = mapped_column(String(20), unique=True)
    representative_name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    address: Mapped[Optional[str]] = mapped_column(String(500))
    bank_code: Mapped[Optional[str]] = mapped_column(String(10))
    bank_account: Mapped[Optional[str]] = mapped_column(String(50))
    bank_holder: Mapped[Optional[str]] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(20), default="PENDING")

    # Relationships
    customers: Mapped[List["Customer"]] = relationship(back_populates="merchant")
    bills: Mapped[List["Bill"]] = relationship(back_populates="merchant")
