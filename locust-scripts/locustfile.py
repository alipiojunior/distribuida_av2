from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5.0, 9.0)

    @task
    def index(self):
        self.client.get("/?p=10")