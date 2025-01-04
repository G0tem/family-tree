from fastapi import APIRouter


app_router = APIRouter(
    prefix="/api/v1",
    tags=["App"]
)

@app_router.get("/app")
async def root():
    return {"message": "Hello World"}
