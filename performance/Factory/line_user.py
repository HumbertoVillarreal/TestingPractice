from locust import HttpUser, task, between
from ..base_user import BaseUser

class LineUser(BaseUser):
    wait_time = between(1,3)

    @task(3)
    def list_lines(self):
        self.client.get("/api/lines/")