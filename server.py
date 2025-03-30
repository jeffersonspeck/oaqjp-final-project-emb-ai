"""File providing the server and route handlers."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detetion_action():
    """Emotion detection handler."""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    emotions = ''.join([f"'{key}': {value}, " for key, value in response.items()])
    if response['dominant_emotion'] is None:
        text = 'Invalid text! Please try again!.'
    else:
        text = f'''
            For the given statement, the system response
            is {emotions}. The dominant emotion 
            is <b>{response['dominant_emotion']}</b>.
        '''
    return text

@app.route("/")
def render_index_page():
    """Index page handler"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
