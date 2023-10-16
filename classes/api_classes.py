from classes.abc_classes import Base
from classes.vacancy import Vacancy
import os
import requests


class HH(Base, Vacancy):
    def __init__(self, keyword, page=0):
        super().__init__(keyword, page)
        self.url: str = 'https://api.hh.ru/vacancies'
        self.params: dict = {
            'text': keyword,
            'page': page
        }

    def get_request(self):
        return requests.get(self.url, params=self.params).json()

    def get_vacancies(self):
        data = self.get_request()
        vacancies = []
        for vacancy in data.get('items', []):
            if vacancy['salary'] is not None:
                vacancy_dict = {
                'name': vacancy['name'],
                'url': vacancy['url'],
                'salary': vacancy.get('salary')['from'],
                'snippet': vacancy['snippet']}
                vacancies.append(vacancy_dict)
        return vacancies


class SJ(Base, Vacancy):
    def __init__(self, keyword, page=0):
        super().__init__(keyword, page)
        self.url: str = 'https://api.superjob.ru/2.0/vacancies/'
        self.params: dict = {
            'text': keyword,
            'page': page
        }

    def get_request(self):
        headers = {
            'X-Api-App-Id': os.getenv('SJ_APIKEY'),
        }
        return requests.get(self.url, headers=headers, params=self.params).json()

    def get_vacancies(self):
        data = self.get_request()
        vacancies = []
        for vacancy in data.get('objects', []):
            if vacancy['payment_from'] is not None:
                vacancy_dict = {
                'name': vacancy['profession'],
                'url': vacancy['link'],
                'salary': vacancy['payment_from'],
                'snippet': vacancy['candidat']}
                vacancies.append(vacancy_dict)
        return vacancies

