from test.conftest import get_client


def test_no_bearer_fail():
    r = get_client().delete('/user/fd7f02dc-8cca-4ed3-bfed-cc42d3c9fe78')
    assert r.status_code == 400
    assert r.json()['detail'] == 'MISSING_AUTH_HEADER'
    pass

def test_bad_bearer_fail():
    r = get_client().delete('/user/fd7f02dc-8cca-4ed3-bfed-cc42d3c9fe78',
        headers={'Authorization': 'Bearer 27da2c7a-1523-4288-1111-5781f36c8c92'}
    )
    assert r.status_code == 400
    assert r.json()['detail'] == 'INVALID_AUTH_TOKEN'
    pass


def test_unauthorized_fail():
    r = get_client().delete(
        '/user/fd7f02dc-8cca-4ed3-bfed-cc42d3c9fe78',
        headers={'Authorization': 'Bearer 27da2c7a-1523-4288-8e46-5781f36c8c92'}
    )
    assert r.status_code == 401
    pass


def test_pass_endpoint():
    r = get_client().delete(
        '/user/fd7f02dc-8cca-4ed3-bfed-cc42d3c9fe78',
        headers={'Authorization': 'Bearer d8837096-c025-4ff0-8e75-839d32e51ec0'}
    )
    assert r.status_code == 200
    pass
