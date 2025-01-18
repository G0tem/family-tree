from typing import Annotated
from authentification.fastapi_users import current_user
from fastapi import APIRouter, Depends
from schemas.UserSchemas import UserRead
from models.UserModel import User


app_router = APIRouter(
    prefix="/api/v1",
    tags=["App"]
)

@app_router.get("/app")
async def root(
    user: Annotated[
        User, 
        Depends(current_user)
        ],
):
    return {"message": "Hello World", "user": UserRead.model_validate(user)}
