import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT_JSON = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL,json=INPUT_JSON, headers=HEADERS)
        
    if response.status_code == 200:
        json_response = json.loads(response.text)
        formatted_response = json_response["emotionPredictions"][0]['emotion']
        emotions_list = []
        scores_list = []
        for emotion, score in formatted_response.items():
            emotions_list.append(emotion)
            scores_list.append(score)
            highest_score_indice = scores_list.index(max(scores_list))
            name_dominant_emotion = emotions_list[highest_score_indice]
        formatted_response['dominant_emotion'] = name_dominant_emotion   
        return formatted_response        
    elif response.status_code == 400:
        formatted_response = {
                               "anger":None,
                               "disgust":None,
                               "fear":None,
                               "joy":None,
                               "sadness":None,
                               "dominant_emotion":None
                             }
        return formatted_response