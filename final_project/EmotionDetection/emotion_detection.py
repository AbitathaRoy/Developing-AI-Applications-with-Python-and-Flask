import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = {"raw_document": {"text": text_to_analyze}}

    response = requests.get(URL, json=Input, headers=Headers)
    formatted_response = json.loads(response)

    if response.status_code == 200:
        score = {
            "anger": formatted_response["documentEmotion"]["anger_score"],
            "disgust": formatted_response["documentEmotion"]["disgust_score"],
            "fear": formatted_response["documentEmotion"]["fear_score"],
            "joy": formatted_response["documentEmotion"]["joy_score"],
            "sadness": formatted_response["documentEmotion"]["sadness_score"]
        }
        dominant_emotion = max(score, key=score.get)
        score["dominant_emotion"] = dominant_emotion

    elif response.status_code == 400:   # Invalid input
        score = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    return score