# Запуск

- minikube start
- запустить скрипт deploy.sh для поднятия рэббита
- ```celery -A app.celery_app.celery_app worker --loglevel=info``` - запустить воркера
- ```kubectl port-forward -n rabbitmq svc/rabbitmq 5672:5672```
- ```kubectl port-forward -n rabbitmq svc/rabbitmq 15672:15672```
- ```uvicorn main:app --host 0.0.0.0 --port 8000```
- ```celery -A app.celery_app.celery_app flower --port=5555 --loglevel=info```
