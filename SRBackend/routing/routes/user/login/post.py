from fastapi import Response

from database.models.User.user import User
from database.main import session
from sqlalchemy import exc

from routing.models.User.loginPost import LoginPost


def handler(data: LoginPost, response: Response):
    user = session.query(User).filter_by(email=data.email).first()

    if user is None:
        response.status_code = 400
        return 'USER_DOES_NOT_EXISTS'

    if user.login(data.password):
        try:
            user_dict = user.as_dict()
            user_dict['roles'] = list(map(lambda x: x.name, user.roles))
            del user_dict['_password'], user_dict['_salt']
            return user_dict
        except exc.SQLAlchemyError as e:
            session.rollback()
            response.status_code = 500
            return str(e.__dict__['orig'])
    else:
        response.status_code = 400
        session.rollback()
        return 'INVALID_PASSWORD'
