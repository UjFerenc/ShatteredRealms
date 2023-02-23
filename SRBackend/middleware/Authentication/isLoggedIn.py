from database.main import session
from database.models.user import User
from sqlalchemy import exc

def check(self):
    if not 'Authorization' in self.headers or not 'Bearer ' in self.headers['Authorization']:
        self.send_response(404, 'Login token was not found')
        return False

    try:
        user = session.execute(User.select(User, User.loginToken, self.headers['Authorization'].split('Bearer ')[0]))
        print(user)
    except exc.SQLAlchemyError as e:
        session.rollback()
        return False

    self.user = user;

    return True
