import requests

from app.celery_app import celery_app
from app.vault_helper import vault_helper

@celery_app.task(name="hello-world-task")
def hello_task():
    return "Hello World!"

@celery_app.task(name="api_request_task")
def api_request_task(alias: str, q: str):
    api_key = None
    headers = {}

    try:
        api_key = vault_helper.get_api_key(alias)
    except Exception as e:
        print("апикей не нужен")

    if alias == 'newsapi':
        url = "https://newsapi.org/v2/everything"
        params = {
            "apikey": api_key,
            "q": q
        }
    elif alias == 'isdayoff':
        try:
            from datetime import datetime
            date_obj = datetime.strptime(q, "%Y-%m-%d")
            year = date_obj.year
            month = date_obj.month
            day = date_obj.day
        except ValueError:
            return {"error": "Invalid date format, expected YYYY-MM-DD"}

        url = "https://isdayoff.ru/api/getdata"
        params = {
            "year": year,
            "month": month,
            "day": day
        }

        response = requests.get(url, params=params)
        result_code = response.json()
        result_word = {
            0: "Рабочий день",
            1: "Нерабочий день",
            2: "Сокращённый рабочий день",
            4: "Рабочий день",
            100: "Ошибка в дате",
            101: "Данные не найдены",
        }.get(result_code, "Неизвестный код ответа")

        return {"date": q, "day_type": result_word}
    elif alias == 'kinopoisk':
        url = "https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword"
        params = {
            "keyword": q
        }
        headers = {
            "X-API-KEY": api_key
        }
    else:
        raise ValueError("Unknown alias")

    response = requests.get(url, params=params, headers=headers)
    return response.json()