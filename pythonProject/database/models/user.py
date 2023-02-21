from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
