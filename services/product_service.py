import requests
from utils.urls import UrlManager, get_token


class ProductService:
    def __init__(self) -> None:
        self.__url_client = UrlManager()
        self.__header: dict = get_token()

    def get_all_products(self) -> dict:
        response = requests.get(
            url=self.__url_client.get_urls_product(),
            headers=self.__header,
            ).json()
        return response
    
    def get_product(self, id: str) -> dict:
        response = requests.get(
            url=self.__url_client.get_urls_product(id),
            headers=self.__header,
            ).json()
        return response
    
    def create_product(self, data) -> dict:
        response = requests.post(
            url=self.__url_client.get_urls_product(),
            json=data,
            headers=self.__header,
            )
        return response
        
    def update_product(self, id, data) -> dict:
        response = requests.patch(
            url=self.__url_client.get_urls_product(id),
            json=data,
            headers=self.__header,
            )
        return response

    def delete_product(self, id):
        response = requests.delete(
            url=self.__url_client.get_urls_product(id),
            headers=self.__header,
            )
        return response.status_code