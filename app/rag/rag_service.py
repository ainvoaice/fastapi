import pandas as pd
import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class ReportRAGService:
    def __init__(self, csv_path: str, embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(embedding_model)
        self.documents = []
        self.embeddings = None
        self.load_csv(csv_path)

    def load_csv(self, path: str):
        df = pd.read_csv(path)
        self.documents = [
            {"content": r["content"], "meta": {"report_id": r["id"], "account_id": r["account_id"]}}
            for _, r in df.iterrows()
        ]
        self.embeddings = np.stack([np.array(json.loads(r["embedding"])) for _, r in df.iterrows()])
        print(f"Loaded {len(self.documents)} documents with embeddings shape {self.embeddings.shape}")

    def retrieve_top_k(self, query: str, k=5):
        # Encode query
        query_emb = self.model.encode([query], convert_to_numpy=True)
        sims = cosine_similarity(query_emb, self.embeddings)[0]
        top_idx = sims.argsort()[-k:][::-1]
        return [self.documents[i] for i in top_idx]
