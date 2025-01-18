from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from models.UserModel import User
from authentification.user_manager import get_user_manager
from authentification.backend import authentication_backend
from schemas.UserSchemas import UserRead, UserCreate, UserUpdate


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)

http_bearer = HTTPBearer(auto_error=False)

user_router = APIRouter(
    prefix="/api/v1",
    dependencies=[Depends(http_bearer)],
    tags=["User"]
)

# /login and /logaut
user_router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
    prefix="/auth",
)

# /register
user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)

# /me and /id
user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
)

# /verify
user_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/verify",
)