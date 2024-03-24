import os

from database.models.User.users import User

client = None

def pytest_configure(config):


    print('pytest config started... ')
    dst_file = './database'

    if os.path.exists(dst_file + '/mydatabase.db'):
        os.remove(dst_file + '/mydatabase.db')

    from main import app
    from fastapi.testclient import TestClient

    global client
    client = TestClient(app)

    setup_dabase_for_tests()

def get_client():
    return client

def get_session():
    from database.main import session
    return session

def setup_dabase_for_tests():
    test_user_delete()

def test_user_delete():
    session = get_session()

    test_user1 = User('test', 'testPassword', is_admin=True)
    test_user1.id = 'fd7f02dc-8cca-4ed3-bfed-cc42d3c9fe78'
    test_user1.loginToken = 'd8837096-c025-4ff0-8e75-839d32e51ec0'
    session.add(test_user1)

    test_user2 = User('test2', 'testPassword', is_admin=False)
    test_user2.id = 'fd7f02dc-8cca-4ed3-bfee-cc42d3c9fe78'
    test_user2.loginToken = 'd8837096-c025-4ff0-0000-839d32e51ec0'
    session.add(test_user2)

    session.commit()