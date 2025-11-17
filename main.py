from uuid import UUID

from celery.result import AsyncResult
from fastapi import FastAPI, Query

from app.celery_app import celery_app
from app.tasks import hello_task, api_request_task

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/task/hello")
def hello_route():
    task = hello_task.delay()
    return {"task_id": task.id}

@app.get("/api/task/check/{task_id}")
def test_check_route(task_id: UUID):
    task = AsyncResult(id=str(task_id), app=celery_app)
    return {
        "id": task.id,
        "status": task.status,
        "result": task.result
    }

# Новый маршрут для запуска задачи API
@app.post("/api/task/execute/")
def execute_api_task(alias: str = Query(...), q: str = Query(...)):
    task = api_request_task.delay(alias, q)
    return {"task_id": task.id}