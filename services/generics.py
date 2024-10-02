import sys
import os

# Adiciona o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from core import settings


class GenericService:
    
    def __get_token(self) -> dict:
        data: dict = {
        "username": self.username,
        "password":  self.password
        }
        response = requests.post(f'{settings.base_url}token/', json=data)
        if response.status_code == 200:
            return response.json().get('access')