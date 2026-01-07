import pytest
from Factory.models import Factory
from unittest.mock import patch

#THIS IS AN EXAMPLE OF MOCK TESTING

@pytest.mark.django_db
@patch("Factory.views.mock_factory")
def test_mock_factory(mock_notify, api_client, user):
    
    api_client.force_authenticate(user=user)

    api_client.post(
        "/api/factories/",
        {"name": "Factory B", "location": "Nuevo Leon"},
        format="json"
    )

    mock_notify.assert_called_once()