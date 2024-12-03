from locust import User , task


class MyFirstTest(User):
    @task
    def launch(self):
        print("Launching the URL")


    @task
    def practice(self):
        print("This is my parctice")




