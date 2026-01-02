# app/api/routes/reports.py
from fastapi import APIRouter, Depends 
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
# from app.haystack.hs_ser_ingestion import ReportEmbeddingService
from app.haystack.hs_ser_embedding import EmbeddingService
from app.haystack.hs_ser_ingestion import ReportEmbeddingService

hsRou = APIRouter()


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