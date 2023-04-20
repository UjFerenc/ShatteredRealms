from test.conftest import get_client

def test_can_call_endpoint():
    r = get_client().delete('/user/asddwdawd')
    assert r.status_code == 404
    pass
