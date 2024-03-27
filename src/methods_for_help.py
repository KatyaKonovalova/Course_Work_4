def filter_vacancies(vacancies, key_words):
    return [vacancy for vacancy in vacancies if
            any(key_word.lower() in vacancy['description'].lower() for key_word in key_words)]
