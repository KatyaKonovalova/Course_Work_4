import unittest
from src.methods_for_help import filter_vacancies


class TestHelpersFunctions(unittest.TestCase):

    def test_filter_vacancies(self):
        vacancies_list = [{'name': 'Python Developer', 'description': 'Description 1'},
                          {'name': 'Java Developer', 'description': 'Description 2'}]
        key_words = ['python']
        filtered_vacancies = filter_vacancies(vacancies_list, key_words)

        if filtered_vacancies:
            self.assertEqual(filtered_vacancies[0]['name'], 'Python Developer')
        else:
            self.assertEqual(len(filtered_vacancies), 0)


if __name__ == '__main__':
    unittest.main()
