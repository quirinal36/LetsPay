from typing import Optional, List
from uuid import UUID
from sqlalchemy import String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin


class Customer(Base, TimestampMixin):
    __tablename__ = "customers"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    merchant_id: Mapped[UUID] = mapped_column(ForeignKey("merchants.id"))
    name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    email: Mapped[Optional[str]] = mapped_column(String(255))
    memo: Mapped[Optional[str]] = mapped_column(String(1000))
    tags: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))

    # Relationships
    merchant: Mapped["Merchant"] = relationship(back_populates="customers")
    bills: Mapped[List["Bill"]] = relationship(back_populates="customer")
