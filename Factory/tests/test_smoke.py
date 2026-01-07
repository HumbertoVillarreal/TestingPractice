import pytest

#THIS IS AN EXAMPLE OF SMOKE TESTING

@pytest.mark.django_db
def test_alive(api_client, user): #Checks if app is alive

    response = api_client.get('/api/factories/')

    assert response.status_code in [200, 401, 403]