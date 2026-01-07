from locust import HttpUser, task, between
from ..base_user import BaseUser

class FactoryUser(BaseUser):
    wait_time = between(1,3)

    @task(3)
    def list_factories(self):
        self.client.get("/api/factories/")