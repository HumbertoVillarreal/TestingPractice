import pytest
from Factory.serializers import FactorySerializer, LineSerializer, MachineSerializer

#THIS IS AN EXAMPLE OF UNIT TESTING

#Test if my serializer works with the factory fixture
@pytest.mark.django_db
def test_factory_serializer_is_valid(factory):

    serializer = FactorySerializer(data={"name":factory.name, "location":factory.location})

    assert serializer.is_valid()

@pytest.mark.django_db
def test_factory_serializer_is_invalid(factory):

    serializer = FactorySerializer(data={"name":factory.name})

    assert not serializer.is_valid()



#Test if my serializer works with the line fixture
@pytest.mark.django_db
def test_line_serializer_is_valid(line):

    serializer = LineSerializer(data={"name": line.name, 
                                      "SN": line.SN,
                                      "machine_qty": line.machine_qty,
                                      "product": line.product,
                                      "factory_id": line.factory_id.id})

    assert serializer.is_valid()

@pytest.mark.django_db
def test_line_serializer_is_invalid(line):

    serializer = LineSerializer(data={"name":line.name})

    assert not serializer.is_valid()



#Test if my serializer works with the machine fixture
@pytest.mark.django_db
def test_machine_serializer_is_valid(line):

    serializer = MachineSerializer(data={"name": "Machine A", 
                                      "SN": "123456789",
                                      "line_id": line.id})

    assert serializer.is_valid()

@pytest.mark.django_db
def test_line_serializer_is_invalid():

    serializer = LineSerializer(data={"name": "Machine A"})

    assert not serializer.is_valid()