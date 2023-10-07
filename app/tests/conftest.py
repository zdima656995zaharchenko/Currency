import pytest
from django.core.management import call_command


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """

@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient
    client = APIClient()
    yield client


@pytest.fixture(scope='function')
def api_client_aut(django_user_model):
    from rest_framework.test import APIClient
    client = APIClient()

    password = 'superSecretPassword'
    user = django_user_model(
        email='example@admin.com',
    )
    user.set_password(password)
    user.save()

    token_response = api_client.post(
        '/api/v1/user/account/token',
        data={'email': user.email, 'password': password},
    )
    assert token_response.status_code == 200
    access = token_response.json()['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'JWT {access}')

    yield api_client

    user.delete()

@pytest.fixture(scope='session', autouse=True)
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = {
            'sources.json',
            'rates.json',
        }
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')
