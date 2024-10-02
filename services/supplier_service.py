import requests
from utils.urls import UrlManager, get_token


class SupplierService:
    def __init__(self) -> None:
        self.__url_client = UrlManager()
        self.__header: dict = get_token()
        
    def get_all_suppliers(self) -> dict:
        response = requests.get(
            url=self.__url_client.get_urls_supplier(),
            headers=self.__header,
            ).json()
        return response
    
    def get_supplier(self, id) -> dict:
        response: dict = requests.get(
            url=self.__url_client.get_urls_supplier(id),
            headers=self.__header,
            ).json()
        return response

    def create_supplier(self, data: dict) -> dict:
        response: dict = requests.post(
            url=self.__url_client.get_urls_supplier(),
            json=data,
            headers=self.__header,
            ).json()
        return response

    def update_supplier(self, id, data) -> dict:
        response: dict = requests.patch(
            url=self.__url_client.get_urls_supplier(id),
            json=data,
            headers=self.__header,
            ).json()
        return response

    def delete_supplier(self, id):
        response: dict = requests.delete(
            url=self.__url_client.get_urls_supplier(id),
            headers=self.__header,
            )
        return response.status_code
