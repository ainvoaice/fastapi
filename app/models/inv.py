from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4
from typing_extensions import Annotated
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List as TypingList

class InvDB(SQLModel, table=True):
    __tablename__ = "invoices"
    
    inv_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    inv_name: str