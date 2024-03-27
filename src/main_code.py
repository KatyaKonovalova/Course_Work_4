from src.hh_ru_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.methods_for_help import filter_vacancies, get_vacancies_based_on_salary
from src.methods_for_help import filter_getting_vacancies, get_number_of_vacancies
from src.methods_for_help import output_vacancies


def user_input():
    platforms = ["HeadHunter"]
    search_request = input("Введите итересующий запрос: ")
    top_n = int(input("Введите нужное число поисковых запросов для вывода: "))
    filter_words = input("Введите ключевые слова для более точного поиска и фильтрации: ").split()
    salary_range = input("Введите интересущий диапазон зарплат (Формат: xxxx-yyyy): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancy(search_request)

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
