import requests
import os
from dotenv import load_dotenv


class VaultHelper:
    def __init__(self):
        load_dotenv(".env")
        self.__vault_addr = os.getenv("VAULT_ADDR")
        self.__token = os.getenv("VAULT_TOKEN")


    def __get_secrets(self, secret_path: str):
        resp = requests.get(
            url=f"{self.__vault_addr}/v1/secrets/data/{secret_path}",
            headers={
                'X-Vault-Token': self.__token
            }
        )

        json_data = resp.json()
        return json_data["data"]["data"]

    def get_rabbitmq_credentials(self) -> dict:
        return self.__get_secrets("rabbitmq")

    def get_api_key(self, alias: str) -> str:
        api_data = self.__get_secrets("apikeys")
        return api_data[alias]


vault_helper = VaultHelper()
