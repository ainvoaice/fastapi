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
                date,
                lead_owner,
                source,
                deal_stage,
                account_id,
                first_name,
                last_name,
                company
            FROM reports
        """))

        rows = result.fetchall()

        documents = []

        for r in rows:
            content = (
                f"Date: {r.date}, "
                f"Lead Owner: {r.lead_owner}, "
                f"Source: {r.source}, "
                f"Deal Stage: {r.deal_stage}, "
                f"Account Id: {r.account_id}, "
                f"First Name: {r.first_name}, "
                f"Last Name: {r.last_name}, "
                f"Company: {r.company}"
            )

            documents.append(
                Document(
                    content=content,
                    meta={
                        "account_id": r.account_id,
                        "deal_stage": r.deal_stage
                    }
                )
            )

        # Embed
        embedded_docs = embedder.run(documents)["documents"]

        # Store in pgvector
        document_store.write_documents(embedded_docs)

        return len(embedded_docs)
