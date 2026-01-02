import pandas as pd
import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


from datetime import datetime
from app.db.models.m_report import Report
from app.db.repo.repo_report import ReportRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, update


class ReportRAGService:
    def __init__(self, csv_path: str, embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(embedding_model)
        self.documents = []
        self.embeddings = None
        self.load_csv(csv_path)

    @staticmethod
    async def list_reports(
        db: AsyncSession,
    ):
        return await ReportRepository.list_reports(db)


    def retrieve_top_k(self, query: str, k=5):
        # Encode query
        query_emb = self.model.encode([query], convert_to_numpy=True)
        sims = cosine_similarity(query_emb, self.embeddings)[0]
        top_idx = sims.argsort()[-k:][::-1]
        return [self.documents[i] for i in top_idx]
