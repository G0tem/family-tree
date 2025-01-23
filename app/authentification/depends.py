from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.UserModel import User
from models.AccessTokenModel import AccessToken
from database import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield User.get_db(session=session)


async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
):
    yield AccessToken.get_db(session=session)
