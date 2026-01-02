# app/service/ser_report_embed.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from haystack import Document

from .hs_store import document_store
from .hs_embedder import embedder


class ReportEmbeddingService:

    @staticmethod
    async def embed_all_reports(db: AsyncSession):
        result = await db.execute(text("""
            SELECT
                id,
                account_id,
                content
            FROM reports
        """))

        rows = result.fetchall()

        if not rows:
            return 0

        documents = [
            Document(
                content=r.content,
                meta={
                    "account_id": r.account_id,
                    "report_id": str(r.id),
                    "source": "reports",
                },
            )
            for r in rows
        ]

        # Embed
        embedded_docs = embedder.run(documents=documents)["documents"]

        # Persist vectors
        document_store.write_documents(embedded_docs)

        return len(embedded_docs)
