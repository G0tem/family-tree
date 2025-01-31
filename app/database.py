from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import (
    POSTGRES_HOST,
    POSTGRES_DB,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
    MONGO_URL,
)
from sqlalchemy.orm import declarative_base
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from pymongo import MongoClient


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


# Подключение к MongoDB
client = MongoClient(MONGO_URL)
db = client["mydatabase"]
collection = db["items"]
