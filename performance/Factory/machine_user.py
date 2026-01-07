from locust import HttpUser, task, between
from ..base_user import BaseUser

class MachineUser(BaseUser):
    wait_time = between(1,3)

    @task(3)
    def list_machines(self):
        self.client.get("/api/machines/")