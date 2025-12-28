# app/db/base.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import validator
import pytz


class TimestampMixin(SQLModel):
    """Mixin for created_at and updated_at timestamps"""
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(pytz.UTC),
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(pytz.UTC),
        nullable=False
    )
    
    @validator('updated_at', pre=True, always=True)
    def update_timestamp(cls, v):
        return v or datetime.now(pytz.UTC)


class UUIDMixin(SQLModel):
    """Mixin for UUID primary key"""
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False
    )


class SoftDeleteMixin(SQLModel):
    """Mixin for soft deletion"""
    is_deleted: bool = Field(default=False, nullable=False)
    deleted_at: Optional[datetime] = None


class AuditMixin(SQLModel):
    """Mixin for audit fields"""
    created_by: Optional[UUID] = None
    updated_by: Optional[UUID] = None


# Base Model combining common mixins
class BaseModel(UUIDMixin, TimestampMixin, SQLModel):
    """Base model for all table models"""
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }


# Base for Pydantic-only models (non-table)
class BaseSchema(SQLModel):
    """Base for Pydantic schemas (non-table models)"""
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }


# If you need a base with soft delete
class SoftDeleteBase(UUIDMixin, TimestampMixin, SoftDeleteMixin, SQLModel):
    """Base model with soft delete capability"""
    pass