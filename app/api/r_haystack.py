# app/api/routes/reports.py
from fastapi import APIRouter, Depends 
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
# from app.haystack.hs_ser_ingestion import ReportEmbeddingService
from app.haystack.hs_ser_embedding import EmbeddingService
from app.haystack.hs_ser_ingestion import ReportEmbeddingService

import openai,os

from app.rag import rag_service

openai.api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
model = "gpt-4o"


hsRou = APIRouter()


class AIRequest(BaseModel):
    query: str

@hsRou.post("/embed_here")
async def action(
    value: int,
    db: AsyncSession = Depends(get_db),
):
    if value == 8:
        count = EmbeddingService().run()
        return {"status": "embedding done", "count": count}

    if value == 9:
        count = await ReportEmbeddingService().embed_all_reports(db)
        return {"status": "embedding done", "reports count": count}


    return {"message": "hello"}




# class QueryRequest(BaseModel):
#     question: str

# # Initialize assistant
# assistant_service = ReportAssistantService()

# @hsRou.post("/ask")
# async def ask_question(request: QueryRequest):
#     question = request.question.strip()
#     if not question:
#         raise HTTPException(status_code=400, detail="Question cannot be empty.")

#     # Run the assistant service
#     answer = await asyncio.to_thread(assistant_service.answer_question, question)
#     return {"answer": answer}



@hsRou.post("/ask")
async def ask_ai(req: AIRequest):
    # 1️⃣ Retrieve top-k relevant reports
    top_docs = rag_service.retrieve_top_k(req.query, k=5)
    context = "\n".join([f"{d['content']}" for d in top_docs])

    messages = [
        {"role": "system", "content": "You are a helpful data assistant. Use the given reports to answer questions concisely and clearly."},
        {"role": "user", "content": f"Based on the following reports:\n{context}\n\nAnswer this question: {req.query}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.2
    )


    response = client.chat.completions.create(
            model=model,
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system",  "content": prompt},
                {"role": "user",    "content": prompt}  
            ],
            temperature=0.0,
        )
        # return response.choices[0].message.content

    return {"answer": response.choices[0].message.content}