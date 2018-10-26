import time
from celery_app import app

@app.task
def add(x,y):
    print("task1.....")
    time.sleep(10)
    return x+y