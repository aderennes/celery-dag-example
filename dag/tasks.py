import time
from datetime import datetime
from celery import Celery

app = Celery(
    'test',
    broker='amqp://admin:mypass@rabbit:5672',
    backend='rpc://'
)


@app.task
def task_a1():
    print(datetime.now(), "Starting task A1")
    time.sleep(2)
    return "Task A1 over"


@app.task
def task_a2():
    print(datetime.now(), "Starting task A2")
    time.sleep(3)
    return "Task A2 over"


@app.task
def task_b():
    print(datetime.now(), "Starting task B")
    time.sleep(2)
    return "Task B over"
