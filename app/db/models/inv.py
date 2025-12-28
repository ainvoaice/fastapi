# app/models/user.py
from __future__ import annotations

from typing import Optional, List
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base, BaseMixin

class Invoice(Base, BaseMixin):
    __tablename__ = "invoice"
    invoice_number: Mapped[str]
    customer_name: Mapped[str]
    total_amount: Mapped[float]

    items_map: Mapped[List["InvoiceItem"]] = relationship(back_populates="invoice_map", lazy="selectin")


class InvoiceItem(Base, BaseMixin):
    __tablename__ = "invoice_item"
    description: Mapped[str]
    quantity: Mapped[float]
    unit_price: Mapped[float]

    invoice_id: Mapped[Optional[UUID]] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("invoice.id", ondelete="SET NULL"), nullable=True
    )

    invoice_map: Mapped[Optional[Invoice]] = relationship(back_populates="items_map", lazy="selectin")