from test.conftest import get_client


def test_creates_if_none():
    r = get_client().post('/user/register', json={'email': 'asd@asd.asd', 'password': 'password'})
    assert r.status_code == 200
    pass


def test_fails_if_created():
    r = get_client().post('/user/register', json={'email': 'asd@asd.asd', 'password': 'password'})
    assert r.status_code == 400
    pass
