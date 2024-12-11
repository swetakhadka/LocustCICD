from locust import HttpUser, TaskSet, task
from locust import between
class UserBehavior(TaskSet):
    @task(2)
    def browse_home(self):
        self.client.get("https://www.daraz.com.np/#?")

    @task(1)
    def search_in_daraz(self):
        self.client.get("https://sellercenter.daraz.com.np/apps/seller/login")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)


