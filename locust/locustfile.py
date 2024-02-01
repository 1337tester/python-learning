from locust import HttpLocust, TaskSet, task

# locust -f locustfile.py --host=http://www.1337tester.com

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self.login()
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        # self.logout()
        pass

    # def login(self):
    #     self.client.post("/login", {"username":"ellen_key", "password":"education"})
    #
    # def logout(self):
    #     self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    @task(1)
    def search(self):
        self.client.get("/search")

    @task(2)
    def robots(self):
        self.client.get("/robots.txt")

    @task(3)
    def sitemap(self):
        self.client.get("/sitemap.xml")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
