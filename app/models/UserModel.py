from fastapi_users.db import SQLAlchemyBaseUserTable
from database import Base
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)