from celery import Celery


celery_app = Celery(
    "worker", broker="redis://redis:6379/0", backend="redis://redis:6379/0"
)


@celery_app.task
def process_data(data: str):
    # Имитация длительной задачи
    import time

    time.sleep(25)
    return f"Processed: {data}"
