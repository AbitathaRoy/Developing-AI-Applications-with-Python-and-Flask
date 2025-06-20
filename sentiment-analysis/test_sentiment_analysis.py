import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        expected_response = [
            {"label": "SENT_POSITIVE"},
            {"label": "SENT_NEGATIVE"},
            {"label": "SENT_NEUTRAL"}
        ]
        actual_response = []
        inputs = ["I love working with Python", "I hate working with Python", "I am neutral on Python"]

        for input in inputs:
            response = sentiment_analyzer(input)
            actual_response.append({"label": response["label"]})

        self.assertEqual(actual_response, expected_response)
if __name__ == "__main__":
    unittest.main()