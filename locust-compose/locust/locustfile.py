#! /usr/bin/python
# -*- coding: utf8 -*-

from locust import HttpLocust, TaskSet, task, events
from stats import stats


class Postman_TaskSet(TaskSet):
    def on_start(self):
        self.client.get("/basic-auth", auth=('postman', 'password'))

    @task(1)
    def Get(self):
        self.client.get("/get?test=123")

    @task(1)
    def Post(self):
        self.client.post("/post", {"one": 1, "two": 2})


class MyLocust(HttpLocust):
    host = 'https://postman-echo.com'
    task_set = Postman_TaskSet
    min_wait = 10000
    max_wait = 30000


# Initialize and run the stats reporting
def reporting():
    s = stats()
    s.start()

events.master_start_hatching += reporting