from fastapi import APIRouter
from tasks.worker import process_data


tasks_router = APIRouter(
    prefix="/api/v1",
    tags=["Tasks"]
)

@tasks_router.post("/process")
async def create_task(data: str):
    task = process_data.delay(data)
    return {"message": "Task created", "task_id": task.id}
