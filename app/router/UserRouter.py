from fastapi_users import FastAPIUsers
from fastapi import APIRouter
from models.UserModel import User
from authentification.user_manager import get_user_manager
from authentification.backend import authentication_backend
from schemas.UserSchemas import UserRead, UserCreate


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)

user_router = APIRouter(
    prefix="/api/v1",
    tags=["User"]
)

# login and logaut
user_router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
    prefix="/auth",
)

# register
user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)