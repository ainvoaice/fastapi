from celery import Celery

celery_app = Celery(
    "celeary",
    broker="redis://localhost:8080/0",
    backend="redis://localhost:8080/0",
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
)
