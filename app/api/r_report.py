# app/api/routes/reports.py
from fastapi import APIRouter, Depends, UploadFile, File, Query
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


@reportRou.get("/pages")
async def list_reports(
    db: AsyncSession = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
    query: str | None = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
):
    return await ReportService.reports_pagination(
        db=db,
        page=page,
        page_size=page_size,
        query=query,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    
    
# FastAPI PATCH endpoint (required)
@reportRou.patch("/{report_id}")
async def update_report(
    report_id: str,
    payload: dict,
    db: AsyncSession = Depends(get_db),
):
    return await ReportService.update_partial(db, report_id, payload)
