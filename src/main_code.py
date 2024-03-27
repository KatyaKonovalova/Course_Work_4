from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.utils.helpers import print_vacancies
from src.utils.helpers import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies


def user_input():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите нужное число поисковых запросов для вывода: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Формат: xxxx-yyyy): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)

    print("Ответ по запросу:", hh_vacancies)

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

        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    else:
        print("Не удалось найти нужные вакансии. Пожалуйста, перепроверьте введенные данные и попробуйет снова.")

    if __name__ == "__main__":
        user_input()
        print("Программа завершила выполнение.")





def filter_vacancies(vacancies, key_words):
    return [vacancy for vacancy in vacancies if
            any(key_word.lower() in vacancy['description'].lower() for key_word in key_words)]


def get_vacancies_by_salary(vacancies, salary_range):
    if not salary_range:
        return vacancies
    salary_value = salary_range.split('-')
    if len(salary_value) == 1:
        minimum_wage = maximum_wage = int(salary_value[0])
    elif len(salary_value) == 2:
        minimum_wage, maximum_wage = map(int, salary_value)
    else:
        print("Введен неверный формат диапазона зарплат.")
        return vacancies

    return [vacancy for vacancy in vacancies if
            vacancy.get('salary_from', 0) >= minimum_wage and vacancy.get('salary_from',
                                                                          float('inf')) <= maximum_wage]


def sort_vacancies(vacancies):
    return sorted(vacancies, key=lambda vacancy: vacancy.get('salary_from', 0), reverse=True)


def get_top_vacancies(vacancies, upper_limit):
    return vacancies[:upper_limit]


def print_vacancies(vacancies):
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано.')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана.')}")
            print(f"Описание: {vacancy.get('description', 'Не указано.')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана.')}")
            print()
    else:
        print("По вашему запросу нет подходящих вакансий.")
