# Sentiment AI - NLP Sentiment Analysis

A full-stack Artificial Intelligence application that analyzes text and predicts sentiment using Natural Language Processing and Machine Learning.

The project combines an ML model, Flask REST API backend, and a modern interactive frontend to provide real-time sentiment predictions.

## 🚀 Live Demo

Frontend Application:

https://sentient-chi.vercel.app

Backend API:

https://sentiment-analysis-ai-o73k.onrender.com

---

## 📌 Project Overview

Sentiment AI is designed to understand the emotional tone of user-provided text.

The application accepts text input and classifies it into:

- Positive Sentiment
- Negative Sentiment

It demonstrates the complete machine learning deployment pipeline:

User Input → Frontend → Flask API → ML Model → Prediction Result

---

## ✨ Features

- Real-time sentiment prediction
- NLP-based text analysis
- Machine Learning classification
- REST API backend
- Interactive web interface
- Cloud deployment
- Responsive user experience

---

## 🛠️ Technologies Used

### Machine Learning
- Python
- Pandas
- Scikit-learn
- Natural Language Processing
- TF-IDF Vectorization
- Logistic Regression

### Backend
- Flask
- Flask-CORS
- Gunicorn

### Frontend
- Next.js
- React
- Tailwind CSS
- Vercel Deployment

---

## 📂 Project Structure
Sentiment-Analysis │ ├── app.py ├── train_model.py ├── sentiment_dataset.csv ├── sentiment_model.pkl ├── requirements.txt ├── README.md └── .gitignore

---

## ⚙️ How It Works

1. User enters a sentence in the web application.
2. Frontend sends the text to the Flask API.
3. Backend processes the input.
4. Machine Learning model analyzes the text.
5. Predicted sentiment is returned and displayed.

---

## 🔌 API Endpoint

### POST
/predict

Example Request:

```json
{
  "text": "I love this product"
}
Example Response:
{
  "text": "I love this product",
  "sentiment": "Positive"
}
💻 Running Locally
Clone the repository:
git clone YOUR_GITHUB_REPOSITORY_URL
Install dependencies:
pip install -r requirements.txt
Train the model:
python train_model.py
Run Flask API:
python app.py
🎯 Future Improvements
Larger real-world sentiment datasets
Multi-class emotion detection
Model performance optimization
Sentiment analytics dashboard
👩‍💻 Author
Mansi Singh
B.Tech Data Science
Machine Learning | Artificial Intelligence | Data Science Projectsv
