import requests

ENDPOINT = 'http://localhost:8000'


def test_can_call_endpoint():
    r = requests.get(ENDPOINT)
    assert r.status_code == 200
    pass


def test_creates_if_none():
    r = requests.post(ENDPOINT + '/user/register', json={'email': 'asd@asd.asd', 'password': 'password'})
    assert r.status_code == 200
    pass


def test_fails_if_created():
    r = requests.post(ENDPOINT + '/user/register', json={'email': 'asd@asd.asd', 'password': 'password'})
    assert r.status_code == 400
    pass
