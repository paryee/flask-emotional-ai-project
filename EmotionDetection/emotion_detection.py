import requests
import json

def emotion_detector(text_to_analyse):
    # Check for blank entries
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        formatted_response = response.json()
        
        # Extract required emotions and their scores
        emotions = formatted_response.get('documentSentiment', {}).get('emotions', [])
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }
        
        for emotion in emotions:
            emotion_name = emotion.get('name', '').lower()
            if emotion_name in emotion_scores:
                emotion_scores[emotion_name] = emotion.get('score', None)
        
        # Determine dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Prepare output format
        output = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        # Handle blank entries or other bad requests
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Handle other errors
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    return output
