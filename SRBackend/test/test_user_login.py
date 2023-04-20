from test.conftest import get_client

def test_if_can_register_to_login():
    r = get_client().post('/user/register', json={'email': 'login@test.test', 'password': 'password'})
    assert r.status_code == 200
    pass

def test_if_can_login_with_regitered():
    r = get_client().post('/user/login', json={'email': 'login@test.test', 'password': 'password'})
    assert r.status_code == 200
    pass

def test_if_has_roles_with_registered():
    r = get_client().post('/user/login', json={'email': 'login@test.test', 'password': 'password'})
    assert 'roles' in r.json().keys()
    assert 'user' in r.json()['roles']
    pass
