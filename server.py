from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detection():
    text = request.args.get('textToAnalyze')
    if not text or text.strip() == "":
        return {"anger": None,"disgust": None,"fear": None,"joy": None,"sadness": None,"dominant_emotion": None}, 400
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400
    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, " f"'disgust': {result['disgust']}, 'fear': {result['fear']}, " f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
 f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response


@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)