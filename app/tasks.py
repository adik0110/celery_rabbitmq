import requests

from app.celery_app import celery_app
from app.vault_helper import vault_helper

@celery_app.task(name="hello-world-task")
def hello_task():
    return "Hello World!"

@celery_app.task(name="api_request_task")
def api_request_task(alias: str, q: str):
    # Получаем API ключ по alias

    api_key = vault_helper.get_api_key(alias)

    # В зависимости от alias выбираем API
    if alias == 'newsapi':
        url = "https://newsapi.org/v2/everything"
        params = {
            "apikey": api_key,
            "q": q
        }
    elif alias == 'newsdata':
        url = "https://newsdata.org/api/1/latest"
        params = {
            "apikey": api_key,
            "q": q
        }
    else:
        raise ValueError("Unknown alias")

    response = requests.get(url, params=params)
    return response.json()