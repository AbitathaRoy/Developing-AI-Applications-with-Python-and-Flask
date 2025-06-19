import requests

def sentiment_analyzer(text_to_analyze):
    URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    Headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    Input = {"raw_document": {"text": text_to_analyze}}     # this library handles I/O as objects

    response = requests.post(URL, json=Input, headers=Headers)
    return response.text
