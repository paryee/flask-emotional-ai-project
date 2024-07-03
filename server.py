"""Flask application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("emotion detector")

@app.route("/emotiondetector")
def sent_analyzer():
    """
    Analyzes the emotion of the given text.

    Returns:
        str: A message with the identified emotion and its score.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return (
        f"The given text has been identified as {dominant_emotion} with a score of "
        f"{response[dominant_emotion]}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page.

    Returns:
        str: The HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
