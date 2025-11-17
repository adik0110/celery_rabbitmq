import requests
import os
from dotenv import load_dotenv


class VaultHelper:
    def __init__(self):
        load_dotenv("../.env")
        self.__vault_addr = os.getenv("VAULT_ADDR")
        self.__token = self.__get_client_token()

    def __get_client_token(self) -> str:
        # resp = requests.post(
        #     url=f"{self.__vault_addr}v1/auth/approle/login",
        #     json={
        #         "role_id": os.getenv("VAULT_ROLE_ID"),
        #         "secret_id": os.getenv("VAULT_SECRET_ID"),
        #     }
        # )

        # json_data = resp.json()
        # return json_data["auth"]["client_token"]

        return 'token123'

    def __get_secrets(self, secret_path: str):
        # resp = requests.get(
        #     url=f"{self.__vault_addr}v1/secrets/data/{secret_path}",
        #     headers={
        #         'X-Vault-Token': self.__vault_token
        #     }
        # )

        # json_data = resp.json()
        # return json_data["data"]["data"]
        d = {
            'rabbitmq': {
                'username': 'username',
                'password': 'password'
            },
            'apikeys': {
                'kinopoisk': '4962088e-c67f-4117-9b05-bc4329727449'
            }
        }

        return d[secret_path]

    def get_rabbitmq_credentials(self) -> dict:
        return self.__get_secrets("rabbitmq")

    def get_api_key(self, alias: str) -> str:
        api_data = self.__get_secrets("apikeys")
        return api_data[alias]


vault_helper = VaultHelper()
