import requests
from utils.urls import UrlManager, get_token


class CategoryService:
    def __init__(self) -> None:
        self.__url_client = UrlManager()
        self.__header: dict = get_token()
        
    def get_all_categories(self):
        response = requests.get(
            url=self.__url_client.get_urls_category(),
            headers=self.__header
            ).json()
        return response
    
    def get_category(self, id):
        response: dict = requests.get(
            url=self.__url_client.get_urls_category(id),
            headers=self.__header
            ).json()
        return response

    def create_category(self, data):
        response: dict = requests.post(
            url=self.__url_client.get_urls_category(),
            json=data,
            headers=self.__header,
            ).json()
        return response

    def update_category(self, id, data):
        response: dict = requests.patch(
            url=self.__url_client.get_urls_category(id),
            json=data,
            headers=self.__header,
            ).json()
        return response

    def delete_category(self, id):
        response: dict = requests.delete(
            url=self.__url_client.get_urls_category(id),
            headers=self.__header,
            )
        return response.status_code


if __name__ == '__main__':
    data: dict = {
    'name': 'Uno',
    'description': 'bem bvom',
    }
    c = CategoryService()
    #print(c.create_category(data=data))
    print(c.get_all_categories())
    print()
    # print(c.get_category(19))
    # print(c.delete_category(19))
    # print(c.get_category(19))

