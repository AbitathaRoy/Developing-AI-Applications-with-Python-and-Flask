"""Web app to perform emotion detection on a given text input"""
from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """Capture user input, send GET request to the model and collect the emotion output."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    output = f"For the given statement, the system response is 'anger': {response['anger']}, "
    output += f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    output += f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    output += f"The dominant emotion is {response['dominant_emotion']}."

    return output

@app.route("/")
def load_index_page():
    """Render the index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
