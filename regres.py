from locust import HttpUser, constant , task
class Myresq(HttpUser):
    host = "https://detech.com.np/"
    wait_time = constant(1)

    @task
    def home_page(self):
        self.client.get("/")
    @task
    def load_career_page(self):
        self.client.get("/career")



