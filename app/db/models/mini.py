# app/models/user.py
from __future__ import annotations

from typing import Optional, List
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base, BaseMixin


class Group(Base, BaseMixin):
    __tablename__ = "groups"
    group_name: Mapped[str]
    users_map: Mapped[List["User"]] = relationship(back_populates="group_map", lazy="selectin")



class User(Base, BaseMixin):
    __tablename__ = "users"
    user_name: Mapped[str]

    group_id: Mapped[Optional[UUID]] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("groups.id", ondelete="SET NULL"), nullable=True
    )

    group_map: Mapped[Optional[Group]] = relationship(back_populates="users_map", lazy="selectin")
