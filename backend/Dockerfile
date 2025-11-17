# Используем официальный Python образ как базу
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта внутрь контейнера
COPY requirements.txt .
COPY app ./app/
COPY main.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000 для FastAPI
EXPOSE 8000
# Открываем порт 5555 для Flower (если нужно запускать внутри контейнера)
EXPOSE 5555

# Команда по умолчанию для запуска FastAPI с Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]