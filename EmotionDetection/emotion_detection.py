import requests
import json
def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inp_json= { "raw_document": { "text": text_to_analyse } }
    response=requests.post(url,json=inp_json,headers=header)
    res_json=json.loads(response.text)
    if response.status_code==200:
        res_dict={
        'anger':res_json["emotionPredictions"][0]["emotion"]["anger"],
        'disgust':res_json["emotionPredictions"][0]["emotion"]["disgust"],
        'fear':res_json["emotionPredictions"][0]["emotion"]["fear"],
        'joy':res_json["emotionPredictions"][0]["emotion"]["joy"],
        'sadness':res_json["emotionPredictions"][0]["emotion"]["sadness"]
        }
        dominant_emotion=max(res_dict,key=res_dict.get)
        res_dict['dominant_emotion']=dominant_emotion
    elif response.status_code==400:
        res_dict={
            'anger':None,
            'disgust':None,
            'fear':None,
            'joy':None,
            'sadness':None,
            'dominant_emotion':None
        }

    return res_dict
