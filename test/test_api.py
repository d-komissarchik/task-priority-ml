import unittest
from fastapi.testclient import TestClient
from main import app

class TestPredictAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_predict_high(self):
        response = self.client.post(
            "/predict",
            json={"task_description": "Fix login bug on website"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["predicted_priority"], "high")

    def test_predict_low(self):
        response = self.client.post(
            "/predict",
            json={"task_description": "Update user profile page"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["predicted_priority"], "low")
