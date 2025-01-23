from typing import Annotated
from authentification.fastapi_users import current_user
from fastapi import APIRouter, Depends
from schemas.UserSchemas import UserRead
from models.UserModel import User


app_router = APIRouter(prefix="/api/v1", tags=["App"])


@app_router.get("/app")
async def root(
    user: Annotated[User, Depends(current_user)],
):
    """
    Router info user, hello

    Args:
        user (Annotated[ User, Depends): authorized user

    Returns:
        _type_: dict
    """
    return {"message": "Hello World", "user": UserRead.model_validate(user)}
