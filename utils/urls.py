import requests
from core import settings


class UrlManager:
    def __format_endpoint_url(self, endpoint_name, id):
        if id:
            url: str = f'{settings.base_url}{endpoint_name}/{id}/'
            return url
        url: str = f'{settings.base_url}{endpoint_name}/'
        return url

    def get_urls_brand(self, id:str = None) -> str:
        endpoint_name = 'brands'
        url = self.__format_endpoint_url(
            endpoint_name=endpoint_name,
            id=id,
            )
        return url

    def get_urls_category(self, id:str = None) -> str:
        endpoint_name = 'categories'
        url = self.__format_endpoint_url(
            endpoint_name=endpoint_name,
            id=id,
            )
        return url
    
    def get_urls_inflow(self, id:str = None) -> str:
        endpoint_name = 'inflows'
        url = self.__format_endpoint_url(
            endpoint_name=endpoint_name,
            id=id,
            )
        return url
    
    def get_urls_outflow(self, id:str = None) -> str:
        endpoint_name = 'outflows'
        url = self.__format_endpoint_url(
            endpoint_name=endpoint_name,
            id=id,
            )
        return url
    
    def get_urls_product(self, id:str = None) -> str:
        endpoint_name = 'products'
        url = self.__format_endpoint_url(
            endpoint_name=endpoint_name,
            id=id,
            )
        return url
    
    def get_urls_supplier(self, id:str = None) -> str:
        endpoint_name = 'suppliers'
        url = self.__format_endpoint_url(
            endpoint_name=endpoint_name,
            id=id,
            )
        return url
    
    
def get_token():
    user_data: dict = {
        'username': settings.username,
        'password':  settings.password
        }
    response = requests.post(f'{settings.base_url}token/', json=user_data)
    if response.status_code == 200:
        access = response.json().get('access')
        token = {
        'Authorization': f'Bearer {access}'
        }
        return token
    