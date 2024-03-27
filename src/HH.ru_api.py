import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    
    @abstractmethod
    def get_vacancy(self, search_query):
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancy(self, search_query):
        params = {"text": search_query, "region": 1}
        response = requests.get(self.base_url, params=params)
        return response.json()
