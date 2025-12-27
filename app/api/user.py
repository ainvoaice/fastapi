# app/api/routes/invoices.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import select, func
from typing import List, Optional
from datetime import date
# from app.models.user import User
from app.models.mini import User
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.database import get_session

router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.get("/user")
async def list_users(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User))
    return result.all()



@router.get("/check")
async def list_users(session: AsyncSession = Depends(get_session)):
    return "hi"
