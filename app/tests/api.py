from rest_framework.test import APIClient

def test_get_api_rates():
    api_client = APIClient()
    response = api_client.get('/api/v1/currency/rates/')
    assert response.status_code == 200