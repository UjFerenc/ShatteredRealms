from database.models.user import User
from database.main import session

def handler(self):
    if hasattr(a, 'jsonData'):
        self.send_response(404, 'JSON data was not found!')
        return

    if not self.jsonData['email']:
        self.send_response(404, 'email parameter was not found!')
        return

    if not self.jsonData['password']:
        self.send_response(404, 'password parameter was not found!')
        return


    user = session.query(User, User.email, post_data['email'])
    if user.login(password):
        try:
            session.update(user)
            session.commit()
            self.status(200)
            self.wfile.write(user)
        except exc.SQLAlchemyError as e:
            self.status(500)
            session.rollback()
    self.status(400)
