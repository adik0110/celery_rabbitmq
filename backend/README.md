# Запуск без кубера

- minikube start
- запустить скрипт deploy.sh для поднятия рэббита
- ```kubectl port-forward -n rabbitmq svc/rabbitmq 5672:5672```
- ```kubectl port-forward -n rabbitmq svc/rabbitmq 15672:15672```
- ```celery -A app.celery_app.celery_app worker --loglevel=info``` - запустить воркера (-P solo если локально) и нужно поменять broker_url
- ```uvicorn main:app --host 0.0.0.0 --port 8000```
- ```celery -A app.celery_app.celery_app flower --port=5555 --loglevel=info```


# Запуск в кубере

- minikube start
- запустить скрипт deploy.sh для поднятия рэббита
- ```kubectl port-forward -n rabbitmq svc/rabbitmq 5672:5672```
- ```kubectl port-forward -n rabbitmq svc/rabbitmq 15672:15672```
- перейти в k8s и прописать ```kubectl apply -f .```
- ```kubectl port-forward svc/backend-service 8000:8000```