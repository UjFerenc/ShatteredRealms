from sqlalchemy import exc
from fastapi import HTTPException, status, Response

from database.main import session
from database.models.user import User
from routing.models.User.registerPost import RegisterPost

tags = ["user"]


def handler(data: RegisterPost, response: Response):

    user = User(data.email, data.password)

    try:
        session.add(user)
        session.commit()
    except exc.IntegrityError as e:
        session.rollback()
        if "UNIQUE constraint failed: user.email" in str(e):
            response.status_code = 400
            return "EMAIL_ALREADY_EXISTS"

    session.commit()
    return 'USER_ADDED'
