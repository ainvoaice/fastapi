# app/api/routes/invoices.py
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.celery.celery_worker import write_log_celery
from app.db.db_async import get_db
from app.db.models.mini import User

userRou = APIRouter(prefix="/user", tags=["user"])


@userRou.get("/user")
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()



@userRou.post("/notify/")
async def notify_user(email: str):
    write_log_celery.delay(f"Notification sent to {email}")
    return {"message": f"Email will be sent to {email}"}

# # app/api/routes/invoices.py
# from fastapi import APIRouter, Depends, HTTPException, status, Query
# from sqlmodel import SQLModel, select, func
# from typing import List, Optional
# from datetime import date
# from uuid import UUID
# # from app.models.user import User
# from app.models.mini import User
# from sqlmodel.ext.asyncio.session import AsyncSession
# from app.db.database import get_session
# from sqlalchemy.orm import selectinload

# router = APIRouter(prefix="/invoices", tags=["invoices"])

# class UserResponse(SQLModel):
#     userid: UUID
#     username: str
#     groupname: Optional[str] = None  # Add groupname field


# @router.get("/user")
# async def list_users(session: AsyncSession = Depends(get_session)):
#     result = await session.exec(select(User))
#     return result.all()



# @router.get("/check")
# async def list_users(session: AsyncSession = Depends(get_session)):
#     # This is NOT a manual join - it's telling SQLAlchemy to load the relationship
#     stmt = select(User).options(selectinload(User.group))
#     result = await session.exec(stmt)
#     users = result.all()
    
#     # Now access directly - NO MANUAL JOIN IN CODE!
#     return [
#         {
#             "username": user.username,
#             "groupname": user.group.groupname if user.group else None  # Direct access!
#         }
#         for user in users
#     ]