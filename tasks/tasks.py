from celery import Celery


app = Celery('tasks', broker='redis://localhost:6379/12', backend='redis://localhost:6379/12')

@app.task
def add(x, y):
    return x + y
