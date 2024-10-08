import requests
from utils.urls import UrlManager, get_token


class BrandService:   
    def __init__(self) -> None:
        self.__url_client = UrlManager()
    
    def get_all_brands(self) -> dict:
        brands = requests.get(
            url=self.__url_client.get_urls_brand(),
            headers=get_token()
            ).json()
        return brands
    
    def get_brand(self, id: str) -> dict:
        brands = requests.get(
            url=self.__url_client.get_urls_brand(id),
            headers=get_token()
            ).json()
        return brands
    
    def create_brand(self, data) -> dict:
        response = requests.post(
            url=self.__url_client.get_urls_brand(),
            headers=get_token(),
            json=data
            ).json()
        return response
        
    def update_brand(self, id: str, data: dict) -> dict:
        response = requests.patch(
        url=self.__url_client.get_urls_brand(id),
        headers=get_token(),
        json=data
        )
        response.raise_for_status()  # Levanta exceção se houver erro HTTP
        return response.json()

    def delete_brand(self, id: str):
        response = requests.delete(
            url=self.__url_client.get_urls_brand(id),
            headers=get_token()
            )
        return response.status_code

