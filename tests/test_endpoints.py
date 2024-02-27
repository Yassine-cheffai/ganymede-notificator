import unittest

from fastapi.testclient import TestClient
from app.main import app


class TestEndpoints(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        return super().setUp()

    def test_bad_email_validation(self):
        """
        Test notifiy endpoint with bad parameters
        """
        response = self.client.post(
            "/", data={"to": "test", "notification_type": "welcome"}
        )
        self.assertEqual(response.status_code, 422)

        response = self.client.post(
            "/", data={"to": "test@mail.com", "notification_type": "some_type"}
        )
        self.assertEqual(response.status_code, 422)
