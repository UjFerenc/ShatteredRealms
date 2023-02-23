from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from database.base import Base

import hashlib, uuid

class User(Base):
    __tablename__ = 'user'

    id = mapped_column(String(10), default=lambda: str(uuid.uuid4()), primary_key=True)
    email: Mapped[str] = mapped_column(String(30), unique=True)
    _password: Mapped[str] = mapped_column(String(256))
    _salt: Mapped[str] = mapped_column(String(256))
    loginToken = mapped_column(String(10), default=lambda: str(uuid.uuid4()))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._salt = uuid.uuid4().hex
        self._password = hashlib.sha512(password.encode('utf-8') + self._salt.encode('utf-8') ).hexdigest()

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def checkPassword(self, password):
        return self._password == hashlib.sha512(password + self._salt).hexdigest()

    def login(self, password):
        if self.checkPassword(password):
            self.loginToken = uuid.uuid4()
            return true
        return false