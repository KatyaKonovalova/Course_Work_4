from src.hh_ru_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.vacancy_actions import JSONAction
from src.methods_for_help import filter_vacancies, get_vacancies_based_on_salary
from src.methods_for_help import filter_getting_vacancies, get_number_of_vacancies
from src.methods_for_help import output_vacancies


def user_input():
    # platform = ["HeadHunter"]
    search_request = input("Введите итересующий запрос: ")
    needed_number_of_vacancies = int(input("Введите нужное число поисковых запросов для вывода: "))
    key_words_for_searching = input("Введите ключевые слова для более точного поиска и фильтрации: ").split()
    salary_range = input("Введите интересущий диапазон зарплат (Формат: xxxx-yyyy): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancy(search_request)

    print("Ответ по запросу:", hh_vacancies)

    vacancies_list = Vacancy.get_vacancy_objects_list(hh_vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, key_words_for_searching)
    ranged_vacancies = get_vacancies_based_on_salary(filtered_vacancies, salary_range)
    sorted_vacancies = filter_getting_vacancies(ranged_vacancies)
    top_vacancies = get_number_of_vacancies(sorted_vacancies, needed_number_of_vacancies)
    output_vacancies(top_vacancies)
    save_file = JSONAction('data/hh_vacancies.json')
    save_file.add_vacancy(hh_vacancies)


if __name__ == "__main__":
    user_input()
    print("Программа завершила выполнение.")
