import unittest
from unittest.mock import patch
from src.hh_ru_api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_vacancies(self, mock_requests_get):
        mock_response = {'items': [{'name': 'Python Developer', 'alternate_url': 'example.com',
                                    'salary': {'from': 100000}, 'description': 'Experience: 3 years'}]}
        mock_requests_get.return_value.json.return_value = mock_response

        hh_api = HeadHunterAPI()
        result = hh_api.get_vacancy('Python Developer')

        self.assertEqual(result, mock_response)


if __name__ == '__main__':
    unittest.main()