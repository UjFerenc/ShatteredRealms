from sqlalchemy.orm import exc
from fastapi import Response, Depends

from database.main import session
from database.models.User.users import User
from dependencies.Authorization.isAdmin import is_admin

tags = ['user']
dependencies = [Depends(is_admin)]

def handler(id: str, response: Response):
    try:
        user = session.get(User, id)
        print(user)
        session.delete(user)
        session.commit()
        return 'USER_DELETED'
    except exc.UnmappedInstanceError as e:
        session.rollback()
        print(str(e))
        if "Class 'builtins.NoneType' is not mapped" in str(e):
            response.status_code = 400
            return 'INVALID_ID'

    response.status_code = 500
    return 'UNKNOWN_ERROR'

