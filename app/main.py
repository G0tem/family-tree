from fastapi import FastAPI
from router.AppRouter import app_router


app = FastAPI()

app.include_router(app_router)