import unittest
from EmotionDetection.emotion_detection import emotion_detector

class MyTestCase(unittest.TestCase):
    def test_emotion_detector(self):
        expected_output = [
            {"dominant_emotion": "joy"},
            {"dominant_emotion": "anger"},
            {"dominant_emotion": "disgust"},
            {"dominant_emotion": "sadness"},
            {"dominant_emotion": "fear"}
        ]
        actual_output = []
        inputs = ["I am glad this happened", "I am really mad about this", "I feel disgusted just hearing about this",
                  "I am so sad about this", "I am really afraid that this will happen"
                  ]

        for input in inputs:
            actual_output.append({"dominant_emotion": emotion_detector(input)})

        self.assertEqual(actual_output, expected_output) 

if __name__ == '__main__':
    unittest.main()
