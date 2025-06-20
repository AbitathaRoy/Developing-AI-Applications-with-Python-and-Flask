import requests
import json

def sentiment_analyzer(text_to_analyze):
    URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    Headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    Input = {"raw_document": {"text": text_to_analyze}}     # this library handles I/O as objects

    response = requests.post(URL, json=Input, headers=Headers)

    # Extract relevant output
    formatted_response = json.loads(response)
    if response.status_code == 200:
        score = formatted_response["documentSentiment"]["score"]
        label = formatted_response["documentSentiment"]["label"]
    elif response.status_code == 500:
        score = None
        label = None

    return {"score": score, "label": label}
