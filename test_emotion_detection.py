import unittest
from flask import Flask
from flask.testing import FlaskClient
from server import app  # Adjust the import based on your file structure

class TestServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = cls.app.test_client()
        cls.client.testing = True

    def test_analyze_emotion_valid(self):
        tests = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        
        for statement, expected_emotion in tests:
            response = self.client.get('/emotiondetector', query_string={'textToAnalyze': statement})
            self.assertIn(f"The given text has been identified as {expected_emotion}", response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

    def test_analyze_emotion_invalid(self):
        response = self.client.get('/emotiondetector', query_string={'textToAnalyze': ''})
        self.assertIn("Invalid text! Please try again!", response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
