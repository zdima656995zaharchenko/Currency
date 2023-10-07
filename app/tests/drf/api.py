from currency.models import Source

def test_get_api_rates(api_client_auth):
    response = api_client_auth.get('/api/v1/rate/list/')
    assert response.status_code == 200
    assert response.json()


def test_post_api_rates_empty(api_client_auth):
    response = api_client_auth.post('/api/v1/rate/list/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sell': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_post_api_rates_valid(api_client_auth):
    source = Source.objects.create(name='test', code_name='test')
    payload = {
        'buy': '30.00',
        'sell': '40.00',
        'source': source.id
    }
    response = api_client_auth.post('api/v1/rate/list', data=payload)
    assert response.status_code == 201

def test_get_source(api_client_auth):
    response = api_client_auth.get("/api/v1/source/list")
    assert response.status_code == 200


def test_get_source_valid_id(api_client_auth):
    response = api_client_auth.get("/api/v1/source/list/?id=2")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 1


def test_get_source_invalid_id(api_client_auth):
    response = api_client_auth.get("/api/v1/source/list/?id=9999")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 0


def test_get_source_invalid_query_param(api_client_auth):
    response = api_client_auth.get("/api/v1/source/list/9999")
    assert response.status_code == 404



