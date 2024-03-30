import unittest
from unittest.mock import patch
from src.vacancy_actions import JSONAction
from src.vacancy import Vacancy


class TestJSONSaverClass(unittest.TestCase):

    @patch('builtins.open', create=True)
    def test_add_vacancy(self, mock_open):
        vacancy = Vacancy("Python Developer", "example.com", "100000-150000", "Experience: 3 years")
        json_action = JSONAction()

        json_action.add_vacancy(vacancy)

        mock_open.assert_called_once_with('vacancies.json', 'a')


if __name__ == '__main__':
    unittest.main()
