# app/api/routes/reports.py
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
from app.service.ser_report import ReportService

reportRou = APIRouter()


@reportRou.post("/upload")
async def upload_reports(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    content = await file.read()
    await ReportService.upload_csv(db, content)
    return {"status": "ok"}


@reportRou.get("/")
async def list_reports(
    db: AsyncSession = Depends(get_db),
):
    return await ReportService.list_reports(db)
