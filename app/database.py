from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.models.AccessTokenModel import AccessToken
from app.models.UserModel import User
from config import POSTGRES_HOST, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USER
from sqlalchemy.orm import declarative_base
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield User.get_db(session=session)

async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
):  
    yield AccessToken.get_db(session=session)
