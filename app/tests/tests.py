import pytest


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.skip('SKIP')
def test_get_rate_list(client):
    response = client.get('/currency/rate/list/')
    assert response.status_code == 200

