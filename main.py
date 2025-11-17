from fastapi import FastAPI

from app.tasks import hello_task

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/task/hello")
def hello_route():
    task = hello_task.delay()
    return {"task_id": task.id}
