from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import List
from uuid import UUID, uuid4

class GroupBase:
    groupname: str

class Group(SQLModel, GroupBase, table=True):
    groupid: UUID = Field(default_factory=uuid4, primary_key=True)
    users: List["User"] = Relationship(back_populates="group")
