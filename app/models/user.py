from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4

class UserBase:
    username: str

class User(SQLModel, UserBase, table=True):
    userid: UUID = Field(default_factory=uuid4, primary_key=True)
    group_id: Optional[UUID] = Field(default=None, foreign_key="group.groupid")
    group: Optional["Group"] = Relationship(back_populates="users")
