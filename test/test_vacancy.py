import unittest
from src.vacancy import Vacancy


class TestVacancyClass(unittest.TestCase):
    def test_vacancy_creation(self):
        vacancy = Vacancy("Python Developer", "example.com", "100000-150000", "Experience: 3 years")

        self.assertEqual(vacancy.title, "Python Developer")
        self.assertEqual(vacancy.link, "example.com")
        self.assertEqual(vacancy.salary, "100000-150000")
        self.assertEqual(vacancy.description, "Experience: 3 years")

    def test_vacancy_creation_with_missing_salary(self):
        vacancy = Vacancy("Python Developer", "example.com", None, "Experience: 3 years")

        self.assertEqual(vacancy.salary, "Зарплата не указана.")

    def test_vacancy_comparison(self):
        vacancy1 = Vacancy("Python Developer", "example1.com", "100000", "Experience: 3 years")
        vacancy2 = Vacancy("Python Developer", "example2.com", "120000", "Experience: 5 years")

        self.assertLess(vacancy1, vacancy2)


if __name__ == '__main__':
    unittest.main()
