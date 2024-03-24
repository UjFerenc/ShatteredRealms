import uuid

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column

from database.base import Base


class PlayerCharacter(Base):
    __tablename__ = 'player_characters'

    id = mapped_column(String(10), default=lambda: str(uuid.uuid4()), primary_key=True)
    user_id = mapped_column(String(), ForeignKey('users.id'))
    name = mapped_column(String(50))
    level = mapped_column(Integer())
    experience = mapped_column(Integer)

    def __init__(self, name, level=1, experience=0):
        self.name = name
        self.level = level
        self.experience = experience
