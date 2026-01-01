# app/api/routes/reports.py
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
# from app.haystack.hs_ser_ingestion import ReportEmbeddingService
from app.service.ser_report import ReportService
from haystack_integrations.document_stores.pgvector import PgvectorDocumentStore
from app.haystack.hs_ser_embedding import EmbeddingService

hsRou = APIRouter()


@hsRou.post("/embed_here")
async def action(value: int):
    if value == 8:
        count = EmbeddingService().run()
        return {"status": "embedding done", "count": count}

    return {"message": "hello"}