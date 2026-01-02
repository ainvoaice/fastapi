import ast
import numpy as np
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

RAG_DOCS: list[dict] = []

async def load_docs_from_pg(session: AsyncSession):
    rows = await session.execute(text("""
        SELECT id, content, embedding
        FROM haystack_documents
        WHERE embedding IS NOT NULL
    """))

    docs = []
    for row in rows.fetchall():
        # parse string to list
        emb_list = ast.literal_eval(row.embedding)
        docs.append({
            "id": row.id,
            "content": row.content,
            "embedding": np.asarray(emb_list, dtype=np.float32),
        })

    RAG_DOCS.clear()
    RAG_DOCS.extend(docs)
