from fastapi import APIRouter
from tasks.worker import process_data


tasks_router = APIRouter(prefix="/api/v1", tags=["Tasks"])


@tasks_router.post("/process")
async def create_task(data: str):
    """
    Test router create task

    Args:
        data (str): str

    Returns:
        _type_: dict, result task, task_id
    """
    task = process_data.delay(data)
    return {"message": "Task created", "task_id": task.id}
