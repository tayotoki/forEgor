from abc import ABC, abstractmethod


class Base(ABC):
    """Получение инф-ии о вакансиях"""
    @abstractmethod
    def get_request(self):
        pass
