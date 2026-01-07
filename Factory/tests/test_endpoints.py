import pytest
from Factory.models import Factory, Line, Machine

#THIS IS AN EXAMPLE OF INTEGRATION TESTING

#Test Factory endpoint POST
@pytest.mark.django_db
def test_create_factory(api_client, user):

    api_client.force_authenticate(user=user)

    response = api_client.post(
        "/api/factories/",
        {"name": "Factory B", "location": "Nuevo Leon"},
        format="json"
    )

    assert response.status_code == 201 #Test if record was created succesfully

    factory = Factory.objects.get(id=response.data["id"]) #Get created record

    assert factory.created_by == user
    
    
#Test Line endpoint POST
@pytest.mark.django_db
def test_create_line(api_client, user, factory):

    api_client.force_authenticate(user=user)

    response = api_client.post(
        "/api/lines/",
        {"name": "Line C", 
            "SN": "123456789",
            "machine_qty": 5,
            "product": "Washer",
            "factory_id": factory.id},
        format="json"
    )

    assert response.status_code == 201 #Test if record was created succesfully

    line = Line.objects.get(id=response.data["id"]) #Get created record

    assert line.created_by == user



#Test Line endpoint POST
@pytest.mark.django_db
def test_create_machine(api_client, user, line):

    api_client.force_authenticate(user=user)

    response = api_client.post(
        "/api/machines/",
        {"name": "Machine C",
         "SN": "123456789",
         "line_id": line.id},
        format="json"
    )

    assert response.status_code == 201 #Test if record was created succesfully

    machine = Machine.objects.get(id=response.data["id"]) #Get created record

    assert machine.created_by == user