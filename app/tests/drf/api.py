from currency.models import Source, Rate

def test_get_api_rates(api_client_auth):
    response = api_client_auth.get("/api/v1/rate/list/")
    assert response.status_code == 200
    assert response.json()


def test_get_api_rate_valid_id(api_client_auth):
    response = api_client_auth.get("/api/v1/rate/list/?id=16")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 1


def test_get_api_rate_invalid_id(api_client_auth):
    response = api_client_auth.get("/api/v1/rate/list/?id=999999")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 0


def test_get_api_rate_invalid_param_format(api_client_auth):
    response = api_client_auth.get("/api/v1/rate/list/16")
    assert response.status_code == 404


def test_post_empty_api_rates(api_client_auth):
    response = api_client_auth.post("/api/v1/rate/list/")
    assert response.status_code == 400
