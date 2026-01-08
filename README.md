# Testing Practice

---
-Practice where I learned how to perform Unit, Smoke, Performance tests as well as fixtures and mocks.


**-Development Environment:** 
* Python 3.11.8.
* Django.

**-Dependencies / Libraries:**
* The required libraries can be found on the *requirements.txt* file on the root of the project. To install these dependencies run the following command on the root of the project:

```bash
# Install requirements.txt libraries
pip install -r requirements.txt
```

### Tests

---

##### /Factory/tests/conftest.py

**-Description:**
* Creates a the fixtures of the api client, database connection as well as some prefabs of the models to work with during the tests.


##### /Factory/tests/test_endpoints.py

**-Description:**
* Implementation of Integration Tests that test and validate that the rest endpoints work correctly and as intended.


##### /Factory/tests/test_mock.py

**-Description:**
* Mocks a call of a method inside a class to test if it´s beign called correctly.


##### /Factory/tests/test_models.py

**-Description:**
* Implementation of Unit Tests that validate that the models work and can create data correctly.


##### /Factory/tests/test_serializers.py

**-Description:**
* Implementation of Unit Tests that validate that the serializers can convert data from the models correctly and are valid.


##### /Factory/tests/test_smoke.py

**-Description:**
* Implementation of a Smoke Test to validate that the app is alive and working correctly to be called.


##### /performace/Factory/*_user.py

**-Description:**
* Group of scripts that create a user that´s gonna be used to call the different endpoint in the performance tests.


##### /performace/base_user.py

**-Description:**
* Script that uses a test user to login do that the perfomance tests can bypass the authentication.


##### /locustfile.py

**-Description:**
* Script that runs the locust web page to do the performance tests (The project must be running to use).


##### /pytest.ini

**-Description:**
* File that indicates the route of the project settings and how the test files are named for pytest-django to look for.


---

### Commands

**-To run project tests**
```bash
pytest
```


**-To run locust and performance tests**
```bash
locust
```
