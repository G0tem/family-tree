from fastapi_users import FastAPIUsers
from fastapi import APIRouter
from app.models.UserModel import User
from app.authentification.user_manager import get_user_manager
from app.authentification.backend import authentication_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)

user_router = APIRouter(
    prefix="/api/v1",
    tags=["User"]
)

user_router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
    prefix="/auth",
)