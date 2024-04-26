import json


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

        if not isinstance(self.salary, (str, int, float)):
            self.salary = "Зарплата не указана"

    def get_vacancy_objects_list(self, hh_vacancies):

        if hh_vacancies and 'items' in hh_vacancies:
            vacancies_list = []

            for vacancy_info in hh_vacancies['items']:

                if isinstance(vacancy_info, dict):
                    name = vacancy_info.get('name', 'Не указано')
                    alternate_url = vacancy_info.get('alternate_url', 'Не указано')
                    salary_info = vacancy_info.get('salary')

                    if salary_info:
                        salary_from = salary_info.get('from', 'Зарплата не указана')
                    else:
                        salary_from = 'Зарплата не указана'
                    description = vacancy_info.get('description', 'Описание отсутствует')
                    vacancies_list.append({'name': name, 'alternate_url': alternate_url, 'salary_from': salary_from,
                                           'description': description})

                elif isinstance(vacancy_info, Vacancy):
                    vacancies_list.append(vacancy_info)

            return vacancies_list
    def __str__(self):
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.link}\nОписание: {self.description}\n"

    def __lt__(self, other):
        return self.salary < other.salary

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Vacancy(data['title'], data['link'], data['salary'], data['description'])
