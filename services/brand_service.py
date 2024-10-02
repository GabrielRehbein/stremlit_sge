import requests
from utils.urls import UrlManager, get_token


class BrandService:   
    def __init__(self) -> None:
        self.__url_client = UrlManager()
        self.__header: dict = get_token()
    
    def get_all_brands(self) -> dict:
        brands = requests.get(
            url=self.__url_client.get_urls_brand(),
            headers=self.__header
            ).json()
        return brands
    
    def get_brand(self, id: str) -> dict:
        brands = requests.get(
            url=self.__url_client.get_urls_brand(id),
            headers=self.__header
            ).json()
        return brands
    
    def create_brand(self, data) -> dict:
        response = requests.post(
            url=self.__url_client.get_urls_brand(),
            headers=self.__header,
            json=data
            ).json()
        return response
        
    def update_brand(self, id: str, data) -> dict:
        response = requests.patch(
            url=self.__url_client.get_urls_brand(id),
            headers=self.__header,
            json=data
            ).json()
        return response

    def delete_brand(self, id: str):
        response = requests.delete(
            url=self.__url_client.get_urls_brand(id),
            headers=self.__header
            )
        return response.status_code


if __name__ == '__main__':
    a = BrandService()
    print(a.get_all_brands())
    print()
    print(a.get_brand(9))