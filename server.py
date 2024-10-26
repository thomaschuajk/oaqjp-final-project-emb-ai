from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route('/')
def render_index_page():
    render_template('/templates/index.html')

@app.route('/emotionDetector')
def sent_detector():
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    system_response = f"For the given statement, the system response is 'anger': ${response['anger']}, 'disgust': ${response['disgust']}, 'fear': ${response['fear']}, 'joy': ${response['joy']} and 'sadness': ${response['sadness']}. The dominant emotion is ${response['dominant_emotion']}."
    return system_response

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
