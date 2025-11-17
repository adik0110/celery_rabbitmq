import os

from dotenv import load_dotenv

def build_broker_url() -> str:
    load_dotenv()
    broker_host = os.getenv("BROKER_HOST", "localhost")
    broker_port = os.getenv("BROKER_PORT", "5672")
    broker_user = os.getenv("BROKER_USER", "username")
    broker_password = os.getenv("BROKER_PASSWORD", "password")

    return f"amqp://{broker_user}:{broker_password}@{broker_host}:{broker_port}/"