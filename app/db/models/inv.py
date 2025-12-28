from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4
from typing_extensions import Annotated
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List as TypingList

class InvoiceDB(SQLModel, table=True):
    __tablename__ = "invoices"
    
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    inv_number: str
    
    # SQLAlchemy 2.0 style with Mapped
    items_map: Mapped[TypingList["InvoiceItemDB"]] = Relationship(
        back_populates="invoice",
        sa_relationship=relationship("InvoiceItemDB", back_populates="invoice")
    )

class InvoiceItemDB(SQLModel, table=True):
    __tablename__ = "inv_items"
    
    userid: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    username: str
    group_id: Optional[UUID] = Field(default=None, foreign_key="group.groupid")
    
    # SQLAlchemy 2.0 style with Mapped
    group: Mapped[Optional["Group"]] = Relationship(
        back_populates="users",
        sa_relationship=relationship("Group", back_populates="users")
    )


# # app/db/models/invoice.py
# from __future__ import annotations
# from sqlmodel import SQLModel, Field, Relationship, Column, JSON
# from typing import Optional, List, Dict, Any
# from datetime import datetime
# from decimal import Decimal
# from uuid import UUID
# import sqlalchemy.dialects.postgresql as pg
# from sqlalchemy.orm import Mapped
# from .base import BaseModel

# class InvoiceBase(SQLModel):
#     """Base schema for Invoice"""
#     invoice_number: str = Field(unique=True, index=True, max_length=50)
#     issue_date: datetime = Field(default_factory=datetime.now)
#     due_date: Optional[datetime] = None
    
#     customer: str = Field(max_length=255)
    
#     # Totals
#     subtotal: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     tax_amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     discount_amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     total_amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     amount_paid: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     balance_due: Decimal = Field(default=0, max_digits=12, decimal_places=2)
    
#     # Status
#     status: str = Field(default="draft", max_length=20)  # draft, sent, paid, cancelled, overdue
    
#     # Additional fields
#     notes: Optional[str] = Field(None, max_length=1000)
#     terms: Optional[str] = Field(None, max_length=500)
#     payment_terms: Optional[str] = Field(None, max_length=100)
    

# class InvoiceDB(BaseModel, InvoiceBase, table=True):

#     """Invoice table model"""
#     __tablename__ = "invoices"
    
#     # Relationships
#     items_map: Mapped[List["InvoiceItemDB"]] = Relationship(
#         back_populates="invoice_map",
#         cascade_delete=True,
#         sa_relationship_kwargs={"lazy": "selectin"}
#     )
    
#     # Computed properties (not stored in DB)
#     @property
#     def is_overdue(self) -> bool:
#         if self.due_date and self.status not in ["paid", "cancelled"]:
#             return datetime.now().date() > self.due_date
#         return False
    
#     @property
#     def payment_status(self) -> str:
#         if self.status == "paid":
#             return "paid"
#         elif self.is_overdue:
#             return "overdue"
#         elif self.amount_paid > 0 and self.amount_paid < self.total_amount:
#             return "partial"
#         elif self.status == "sent":
#             return "pending"
#         else:
#             return self.status



# class InvoiceItemBase(SQLModel):
#     """Base schema for InvoiceItem"""
#     invoice_id: UUID = Field(foreign_key="invoices.id")
#     description: str = Field(max_length=500)
#     quantity: Decimal = Field(max_digits=10, decimal_places=3, ge=0)
#     unit_price: Decimal = Field(max_digits=12, decimal_places=2, ge=0)
#     unit: Optional[str] = Field("pcs", max_length=20)
    
#     # Tax information
#     tax_rate: Decimal = Field(default=18, max_digits=5, decimal_places=2, ge=0)
    
#     # Discount
#     discount_percent: Decimal = Field(default=0, max_digits=5, decimal_places=2, ge=0)
    
#     # Computed fields (will be populated by database triggers or application logic)
#     discount_amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     taxable_amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     tax_amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)
#     total_amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)


# class InvoiceItemDB(BaseModel, InvoiceItemBase, table=True):
#     """InvoiceItem table model"""
#     __tablename__ = "inv_items"
    
#     # Relationships
#     invoice_map: Mapped["InvoiceDB"] = Relationship(back_populates="items_map")
    
#     # Computed properties
#     @property
#     def line_total(self) -> Decimal:
#         """Calculate line total before tax and discount"""
#         return self.quantity * self.unit_price
    
#     @property
#     def line_total_after_discount(self) -> Decimal:
#         """Calculate line total after discount"""
#         discount = self.line_total * (self.discount_percent / 100)
#         return self.line_total - discount

