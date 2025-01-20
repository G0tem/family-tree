from fastapi import FastAPI
from router.AppRouter import app_router
from router.UserRouter import user_router
from router.TasksRouter import tasks_router


app = FastAPI()

app.include_router(app_router)
app.include_router(user_router)
app.include_router(tasks_router)
