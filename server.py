'''This is code implementation for backend service'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Predictor")

@app.route('/')
def render_index_page():
    '''This is the function for rendering the landing page'''
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector():
    '''This is the function for returning the emotion detection analysis'''
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    system_response = f"For the given statement, the system response is \
                    'anger': {response['anger']}, \
                    'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, \
                    'joy': {response['joy']} \
                    and 'sadness': {response['sadness']}. \
                    The dominant emotion is {response['dominant_emotion']}."
    return system_response

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
