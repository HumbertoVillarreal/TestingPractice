import pytest
from Factory.models import Factory, Line
from rest_framework.test import APIClient
from django.contrib.auth.models import User

#THIS IS AN EXAMPLE OF FIXTURE FOR TESTING

#Create a fixture of a factory so line models can be tested with FK
@pytest.fixture
def factory():
    return Factory.objects.create(
        name = "Factory A",
        location = "Monterrey",
    )


#Create a fixture of a line so machine models can be tested with FK
@pytest.fixture
def line(factory):
    return Line.objects.create(
        name = "Line A",
        SN = "123456789",
        machine_qty = 3,
        product = "Motherboard C",
        factory_id = factory
    )



#API Client fixture to call endpoints
@pytest.fixture
def api_client():
    return APIClient()


#Create user to bypass endpoints authorization
@pytest.fixture
def user():
    return User.objects.create_user(
        username="admin",
        password="admin"
    )