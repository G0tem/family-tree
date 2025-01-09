from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from database import Base
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(
                    Integer, 
                    primary_key=True
                )

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
