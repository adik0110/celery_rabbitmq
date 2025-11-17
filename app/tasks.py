# import requests

from app.celery_app import celery_app
# from celery_app import app
# from vault_helper import vault_helper

# CALLBACK_DICT = {
#     'newsapi': lambda api_key, **params: requests.get(
#         "https://newsapi.org/v2/everything",
#         params={"apikey": api_key, **params}
#     ).json(),
#     'newsdata': lambda api_key, **params: requests.get(
#         "https://newsdata.org/api/1/latest",
#         params={"apikey": api_key, **params}
#     ).json(),
# }
#
# @app.task
# def call_api(alias, params):
#     api_key = vault_helper.get_api_key(alias)
#     func = CALLBACK_DICT.get(alias, CALLBACK_DICT['newsapi'])
#     return func(api_key, **params)

@celery_app.task(name="hello-world-task")
def hello_task():
    return "Hello World!"