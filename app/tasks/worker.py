from celery import Celery


celery_app = Celery(
    "worker", broker="redis://0.0.0.0:6379/0", backend="redis://0.0.0.0:6379/0"
)


@celery_app.task
def process_data(data: str):
    # Имитация длительной задачи
    import time

    time.sleep(5)
    time.sleep(20)
    return f"Processed: {data}"
