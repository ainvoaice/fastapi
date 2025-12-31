# app/models/user.py
from __future__ import annotations

from typing import Optional, List
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base, BaseMixin


class Group(Base, BaseMixin):
    __tablename__ = "group"
    group_name: Mapped[str]
    users_map: Mapped[List["User"]] = relationship(back_populates="group_map", lazy="selectin")



class User(Base, BaseMixin):
    __tablename__ = "user"
    user_name: Mapped[str]

    group_id: Mapped[Optional[UUID]] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("group.id", ondelete="SET NULL"), nullable=True
    )

    group_map: Mapped[Optional[Group]] = relationship(back_populates="users_map", lazy="selectin")



class LeadReportDocument(Base, Base):
    __tablename__ = "reports"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    date: Mapped[date] = mapped_column(Date, nullable=False)
    lead_owner: Mapped[str] = mapped_column(String(255), nullable=False)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    deal_stage: Mapped[str] = mapped_column(String(100), nullable=False)
    account_id: Mapped[str] = mapped_column(String(32), nullable=False)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    company: Mapped[str] = mapped_column(String(255), nullable=False)

    content: Mapped[str] = mapped_column(Text, nullable=False)
    embedding: Mapped[list[float]] = mapped_column(Vector(1536), nullable=False)
