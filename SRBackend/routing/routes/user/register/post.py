from sqlalchemy import exc
from fastapi import Response, HTTPException

from database.main import session
from database.models.User.users import User
from routing.models.User.registerPost import RegisterPost

tags = ['user']


def handler(data: RegisterPost, response: Response):

    user = User(data.email, data.password)

    try:
        session.add(user)
        session.commit()
    except exc.IntegrityError as e:
        session.rollback()
        print(str(e))
        if 'UNIQUE constraint failed: users.email' in str(e):
            raise HTTPException(status_code=400, detail='EMAIL_ALREADY_EXISTS')

    session.commit()
    return 'USER_ADDED'
