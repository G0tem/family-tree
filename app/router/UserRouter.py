from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from authentification.backend import authentication_backend
from schemas.UserSchemas import UserRead, UserCreate, UserUpdate
from authentification.fastapi_users import fastapi_users


http_bearer = HTTPBearer(auto_error=False)

user_router = APIRouter(
    prefix="/api/v1",
    dependencies=[Depends(http_bearer)],
    tags=["User"]
)

# /login and /logaut
user_router.include_router(
    fastapi_users.get_auth_router(
        authentication_backend,
        requires_verification=True,
    ),
    prefix="/auth",
)

# /register
user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)

# /me
user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
)

# /verify
user_router.include_router(
    fastapi_users.get_verify_router(UserRead),
)

# /reset-password
user_router.include_router(
    fastapi_users.get_reset_password_router(),
)
