def filter_vacancies(vacancies, key_words):
    return [vacancy for vacancy in vacancies if
            any(key_word.lower() in vacancy['description'].lower() for key_word in key_words)]


def get_vacancies_based_on_salary(vacancies, salary_range):
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


def filter_getting_vacancies(vacancies):
    return sorted(vacancies, key=lambda vacancy: vacancy.get('salary_from', 0), reverse=True)


def get_number_of_vacancies(vacancies, upper_limit):
    return vacancies[:upper_limit]


def output_vacancies(vacancies):
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано.')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана.')}")
            print(f"Описание: {vacancy.get('description', 'Не указано.')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана.')}")
            print()
    else:
        print("На основании введенных данных подходящие вакансии отсутствуют.")



