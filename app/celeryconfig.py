from app.utils import build_broker_url

broker_url = build_broker_url()

imports = ['app.tasks']

result_backend = 'rpc://'