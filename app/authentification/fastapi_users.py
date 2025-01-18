from fastapi_users import FastAPIUsers
from models.UserModel import User
from .user_manager import get_user_manager
from .backend import authentication_backend


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)

current_user = fastapi_users.current_user(active=True)