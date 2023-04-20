import uuid

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from database.base import Base


class Role(Base):
    __tablename__ = 'roles'

    id = mapped_column(String(10), default=lambda: str(uuid.uuid4()), primary_key=True)
    name: Mapped[str] = mapped_column(String(10))

    def __init__(self, name):
        self.name = name