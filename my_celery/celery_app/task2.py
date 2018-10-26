import time
from celery_app import app

@app.task
def multipy(x,y):
    print("task2.....")
    time.sleep(10)
    return x*y