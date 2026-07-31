from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load model
model = pickle.load(open("sentiment_model.pkl", "rb"))


@app.route("/")
def home():
    return jsonify({
        "message": "Sentiment Analysis API Running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    text = data["text"]

    prediction = model.predict([text])[0]

    return jsonify({
        "text": text,
        "sentiment": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)