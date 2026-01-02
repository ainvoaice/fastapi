# app/api/routes/reports.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from app.rag.rag_store import RAG_DOCS  # in-memory docs loaded from PG


import openai, os
from app.rag import rag_service

openai.api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
openaimodel = "gpt-4o"


ragRou = APIRouter()

class AIRequest(BaseModel):
    query: str


@ragRou.post("/ask")
async def ask_ai(req: AIRequest):
    top_docs = rag_service.retrieve_top_k(req.query, k=5)
    context = "\n".join([f"{d['content']}" for d in top_docs])

    messages = [
        {
            "role": "system",
            "content": "You are a helpful data assistant. Use the given reports to answer questions concisely and clearly.",
        },
        {
            "role": "user",
            "content": f"Based on the following reports:\n{context}\n\nAnswer this question: {req.query}",
        },
    ]

    response = client.chat.completions.create(
        model=openaimodel,
        response_format={"type": "json_object"},
        messages=messages,
        temperature=0.2,
    )
    # return response.choices[0].message.content

    return {"answer": response.choices[0].message.content}


class RAGRequest(BaseModel):
    query: str
    top_k: int = 3  # optional, default 3


class RAGResponse(BaseModel):
    answer: str
    sources: list[str]
    
    
# initialize embedding model once
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


@ragRou.post("/purerag", response_model=RAGResponse)
async def purerag_endpoint(req: RAGRequest):
    # 1. Embed the query
    query_emb = model.encode([req.query])[0]

    # 2. Compute cosine similarity with in-memory embeddings
    embeddings = np.array([doc["embedding"] for doc in RAG_DOCS])
    sims = cosine_similarity([query_emb], embeddings)[0]

    # 3. Select top-K documents
    top_k = req.top_k
    top_idx = sims.argsort()[-top_k:][::-1]
    top_docs = [RAG_DOCS[i] for i in top_idx]

    # 4. Concatenate context
    context = "\n\n".join(doc["content"] for doc in top_docs)

    # 5. Build prompt and call LLM (dummy placeholder for now)
    prompt = f"Answer using ONLY the context below.\n\nContext:\n{context}\n\nQuestion:\n{req.query}"
    answer = prompt  # replace with real LLM call

    return RAGResponse(
        answer=answer,
        sources=[doc["id"] for doc in top_docs],
    )