from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import UUID, uuid4

class UserBase(SQLModel):
    username: str

class GroupBase(SQLModel):
    groupname: str

class Group(SQLModel, table=True):
    groupid: UUID = Field(default_factory=uuid4, primary_key=True)
    groupname: str
    # users: List["User"] = Relationship(back_populates="group")

class User(SQLModel, table=True):
    userid: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str
    group_id: Optional[UUID] = Field(default=None, foreign_key="group.groupid")
    # group: Optional[Group] = Relationship(back_populates="users")

# Pydantic v2 forward reference fix
# User.model_rebuild()
# Group.model_rebuild()
