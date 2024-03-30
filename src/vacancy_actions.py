from abc import ABC, abstractmethod
import json


class AbstractVacancyAction(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_based_on_criteria(self, criteria):
        pass


class JSONAction(AbstractVacancyAction):
    def __init__(self, file_path="vacancy.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a') as file:
            json.dump(vars(vacancy), file)
            file.write('\n')

    def delete_vacancy(self, vacancy):
        # Удаления вакансии из файла
        pass

    def get_vacancy_based_on_criteria(self, criteria):
        # Получения вакансий из файла по критерию
        pass
