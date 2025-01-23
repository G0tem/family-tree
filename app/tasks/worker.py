from celery import Celery


celery_app = Celery(
    "worker", broker="redis://0.0.0.0:6379/0", backend="redis://0.0.0.0:6379/0"
)


@celery_app.task
def process_data(data: str):
    # Имитация длительной задачи
    import time

    time.sleep(10)
    return f"Processed: {data}"
