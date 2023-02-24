from database.models.user import User
from database.main import session
from sqlalchemy import exc
import json


def handler(self):
    if not hasattr(self, 'jsonData'):
        self.send_error(404, 'JSON data was not found!')
        return

    if 'email' not in self.jsonData:
        self.send_error(400, 'MISSING_EMAIL_FIELD')
        return

    if 'password' not in self.jsonData:
        self.send_error(400, 'MISSING_PASSWORD_FIELD')
        return

    user = session.query(User).filter_by(email=self.jsonData['email']).first()
    if user.login(self.jsonData['password']):
        try:
            userDict = user.as_dict()
            del userDict['_password'], userDict['_salt']
            self.sendResponse(200, str(json.dumps(userDict)))
        except exc.SQLAlchemyError as e:
            self.send_error(500, str(e.__dict__['orig']))
            session.rollback()
    else:
        self.send_error(400, 'INVALID_PASSWORD')
        session.rollback()
