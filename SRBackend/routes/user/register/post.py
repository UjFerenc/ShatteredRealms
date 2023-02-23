from database.main import session
from database.models.user import User
from sqlalchemy import exc
import json
import uuid

def handler(self):
    if not hasattr(self, 'jsonData'):
        self.sendResponse(404, 'JSON data was not found!')
        return

    if 'email' not in self.jsonData:
        self.send_error(400, 'MISSING_EMAIL_FIELD')
        return

    if 'password' not in self.jsonData:
        self.send_error(400, 'MISSING_PASSWORD_FIELD')
        return

    user = User(self.jsonData['email'], self.jsonData['password'])

    try:
        session.add(user)
        session.commit()
    except exc.SQLAlchemyError as e:
        session.rollback()
        error = str(e.__dict__['orig'])
        self.sendError(500, error)
        return

    session.commit()
    self.sendResponse(200, 'user added')