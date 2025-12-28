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
    groupname: Mapped[str]
    users: Mapped[List["User"]] = relationship(back_populates="group", lazy="selectin")



class User(Base, BaseMixin):
    __tablename__ = "user"
    username: Mapped[str]

    group_id: Mapped[Optional[UUID]] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("group.groupid", ondelete="SET NULL"), nullable=True
    )

    group: Mapped[Optional[Group]] = relationship(back_populates="users", lazy="selectin")
