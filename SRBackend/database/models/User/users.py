import hashlib
import uuid
from typing import List

from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base
from database.models.User.roles import Role

role_association_table = Table(
    'role-association_table',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('role_id', ForeignKey('roles.id'), primary_key=True)
)

player_character_association_table = Table(
    'player_characters-association_table',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('player_character_id', ForeignKey('player_characters.id'), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(String(10), default=lambda: str(uuid.uuid4()), primary_key=True)
    email: Mapped[str] = mapped_column(String(30), unique=True)
    _password: Mapped[str] = mapped_column(String(256))
    _salt: Mapped[str] = mapped_column(String(256))
    loginToken = mapped_column(String(10), default=lambda: str(uuid.uuid4()))
    roles: Mapped[List['Role']] = relationship(secondary=role_association_table)
    playerCharacters: Mapped[List['PlayerCharacter']] = relationship(secondary=player_character_association_table)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._salt = uuid.uuid4().hex
        self._password = hashlib.sha512(password.encode('utf-8') + self._salt.encode('utf-8')).hexdigest()

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = password

        from database.main import session
        user_role = session.query(Role).filter_by(name='user').first()
        if user_role is None:
            user_role = Role('user')

        roles = [user_role]


        if is_admin:
            admin_role = session.query(Role).filter_by(name='admin').first()
            if admin_role is None:
                admin_role = Role('admin')
            roles.append(admin_role)



        self.roles = roles
        self.characters = []

    def checkPassword(self, password):
        return self._password == hashlib.sha512((password + self._salt).encode('utf-8')).hexdigest()

    def login(self, password):
        if self.checkPassword(password):
            self.loginToken = str(uuid.uuid4())
            return True
        return False
