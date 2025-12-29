from celery import Celery
import time

# Configure Celery to use Redis as the message broker
celery = Celery(
    "leo_celery_worker",  # This is the name of your Celery application
    broker="redis://localhost:8080/0",  # This is the Redis connection string
    backend="redis://localhost:8080/0",  # Optional, for storing task results
)


@celery.task
def write_log_celery(message: str):
    time.sleep(30)
    with open("log_celery.txt", "a") as f:
        f.write(f"{message}\n")
    return f"Task completed: {message}"