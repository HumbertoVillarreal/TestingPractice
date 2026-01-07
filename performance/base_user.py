from locust import HttpUser

class BaseUser(HttpUser):

    def on_start(self):

        response = self.client.post("/api/token/", json={"username":"admin", "password":"admin"})
        token = response.json()["token"]

        self.client.headers = {
            "Authorization": f"Token {token}"
        }