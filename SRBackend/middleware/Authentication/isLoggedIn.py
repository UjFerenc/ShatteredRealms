from database.main import session
from database.models.user import User

def check(self):
    if not 'Authorization' in self.headers or not 'Bearer ' in self.headers['Authorization']:
        self.send_response(404, 'Login token was not found')
        return false

    try:
        user = session.execute(User.select(User, User.loginToken, self.headers['Authorization'].split('Bearer ')[0]))
        print(user)
    except exc.SQLAlchemyError as e:
        session.rollback()
        return false

    self.user = user;

    return true
