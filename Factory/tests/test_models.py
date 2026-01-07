import pytest
from Factory.models import Factory, Line, Machine

#THIS IS AN EXAMPLE OF UNIT TESTING

#Tests if Factory is created correctly and its str
@pytest.mark.django_db
def test_factory_str(factory):

    assert str(factory) == "Factory A (Monterrey)"


#Tests if Factory is created correctly and its str
@pytest.mark.django_db
def test_line_str(line):

    assert str(line) == "Line A (123456789)"



#Tests if Factory is created correctly and its str
@pytest.mark.django_db
def test_machine_str(line):
    machine = Machine.objects.create(
        name = "Machine A",
        SN = "123456789",
        line_id = line
    )

    assert str(machine) == "Machine A (123456789)"