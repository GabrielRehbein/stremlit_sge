import requests
from utils.urls import UrlManager, get_token


class InflowService:
    def __init__(self) -> None:
        self.__url_client = UrlManager()

    def get_all_inflows(self) -> dict:
        response = requests.get(
            url=self.__url_client.get_urls_inflow(),
            headers=get_token(),
            ).json()
        return response

    def get_inflow(self, id: str) -> dict:
        response = requests.get(
            url=self.__url_client.get_urls_inflow(id),
            headers=get_token(),
            ).json()
        return response

    def create_inflow(self, data) -> dict:
        response = requests.post(
            url=self.__url_client.get_urls_inflow(),
            json=data,
            headers=get_token(),
            )
        return response

    def update_inflow(self, id, data) -> dict:
        response = requests.patch(
            url=self.__url_client.get_urls_inflow(id),
            json=data,
            headers=get_token(),
            )
        return response

    def delete_inflow(self, id):
        response = requests.delete(
            url=self.__url_client.get_urls_inflow(id),
            headers=get_token(),
            )
        return response.status_code