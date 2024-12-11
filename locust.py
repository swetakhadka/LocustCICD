
from locust import HttpUser, task, between

class DetechWebsiteLoadTest(HttpUser):
    # This simulates a wait time between 1 and 3 seconds between tasks
    wait_time = between(1, 3)

    @task
    def homepage(self):
        # This will simulate a user visiting the homepage of the website
        self.client.get("https://www.detech.com.np/")

    @task
    def about_page(self):
        # This will simulate a user visiting the 'About' page
        self.client.get("https://www.detech.com.np/about")

    @task
    def services_page(self):
        # This will simulate a user visiting the 'Services' page
        self.client.get("https://www.detech.com.np/services")





