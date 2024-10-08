import requests
from utils.urls import UrlManager, get_token


class OutflowService:
    def __init__(self) -> None:
        self.__url_client = UrlManager()
        self.__header: dict = get_token()

    def get_all_outflows(self) -> dict:
        response = requests.get(
            url=self.__url_client.get_urls_outflow(),
            headers=self.__header,
            ).json()
        return response

    def get_outflow(self, id: str) -> dict:
        response = requests.get(
            url=self.__url_client.get_urls_outflow(id),
            headers=self.__header,
            ).json()
        return response

    def create_outflow(self, data) -> dict:
        response = requests.post(
            url=self.__url_client.get_urls_outflow(),
            json=data,
            headers=self.__header,
            )
        return response

    def update_outflow(self, id, data) -> dict:
        response = requests.patch(
            url=self.__url_client.get_urls_outflow(id),
            json=data,
            headers=self.__header,
            )
        return response

    def delete_outflow(self, id):
        response = requests.delete(
            url=self.__url_client.get_urls_outflow(id),
            headers=self.__header,
            )
        return response.status_code