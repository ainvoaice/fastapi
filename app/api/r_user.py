# app/api/routes/invoices.py
from celery.result import AsyncResult
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.celery.celery_worker import write_log_celery
from app.db.db_async import get_db
from app.db.models.mini import User

userRou = APIRouter(prefix="/user", tags=["user"])


@userRou.get("/user")
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()



@userRou.post("/notify/")
async def notify_user(email: str):
    """Endpoint that triggers the background task in Celery."""
    task = write_log_celery.delay(f"Notification sent to {email}")
    # task is a AsyncResult, a promise to a result that will be available later.
    return {"message": f"Email will be sent to {email}", "task_id": task.id}


@userRou.get("/task_status/{task_id}")
async def get_task_status(task_id: str):
    """Endpoint to check the status of the task."""
    task_result = AsyncResult(task_id)  # Get the task result using the task ID
    if task_result.ready():  # If the task is done
        return {"task_id": task_id, "status": "completed", "result": task_result.result}
    elif task_result.failed():  # If the task failed
        return {"task_id": task_id, "status": "failed"}
    else:  # If the task is still in progress
        return {"task_id": task_id, "status": "in progress"}