import unittest
from unittest.mock import patch
from io import StringIO
from src.main_code import user_input


class TestMainInteraction(unittest.TestCase):

    @patch('builtins.input', side_effect=["it", "1", "python", "100000"])
    @patch('src.hh_ru_api.HeadHunterAPI.get_vacancy', return_value={'items': []})
    def test_user_input_no_vacancies(self, mock_input, mock_get_vacancies):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_input()
            self.assertIn("На основании введенных данных подходящие вакансии отсутствуют.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
