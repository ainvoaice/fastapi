from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4
from typing_extensions import Annotated
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List as TypingList

class Group(SQLModel, table=True):
    __tablename__ = "group"
    
    groupid: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    groupname: str
    
    # SQLAlchemy 2.0 style with Mapped
    users: Mapped[TypingList["User"]] = Relationship(
        back_populates="group",
        sa_relationship=relationship("User", back_populates="group")
    )

class User(SQLModel, table=True):
    __tablename__ = "user"
    
    userid: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    username: str
    group_id: Optional[UUID] = Field(default=None, foreign_key="group.groupid")
    
    # SQLAlchemy 2.0 style with Mapped
    group: Mapped[Optional["Group"]] = Relationship(
        back_populates="users",
        sa_relationship=relationship("Group", back_populates="users")
    )