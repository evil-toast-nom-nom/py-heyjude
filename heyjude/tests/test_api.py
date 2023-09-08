import unittest
from unittest.mock import patch, Mock
from ..api import HeyJudeAPI

class TestHeyJudeAPI(unittest.TestCase):

    @patch('heyjude.api.requests.post')
    def test_authenticate(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"token": "sample_token"}
        mock_post.return_value = mock_response

        api = HeyJudeAPI(email="test@example.com", password="test_password", api_key="test_api_key")
        self.assertEqual(api.token, "sample_token")

    @patch('heyjude.api.requests.get')
    def test_refresh_token(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"new_token": "new_sample_token"}
        mock_get.return_value = mock_response

        api = HeyJudeAPI(email="test@example.com", password="test_password", api_key="test_api_key")
        result = api.refresh_token()
        self.assertEqual(result, {"new_token": "new_sample_token"})

    @patch('heyjude.api.requests.get')
    def test_get_subscription_status(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "active"}
        mock_get.return_value = mock_response

        api = HeyJudeAPI(email="test@example.com", password="test_password", api_key="test_api_key")
        result = api.get_subscription_status()
        self.assertEqual(result, {"status": "active"})


if __name__ == "__main__":
    unittest.main()
