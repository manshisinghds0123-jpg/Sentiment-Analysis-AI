# Sentiment Analysis AI

A Machine Learning based Sentiment Analysis application that classifies text into Positive or Negative sentiment.

## Features

- Text sentiment prediction
- Machine Learning model using NLP
- TF-IDF text vectorization
- Logistic Regression classifier
- Flask REST API backend
- Interactive AI frontend

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- NLP
- Machine Learning

## Project Structure
Sentiment-Analysis/ │ ├── app.py ├── train_model.py ├── sentiment_dataset.csv ├── sentiment_model.pkl ├── requirements.txt ├── README.md └── .gitignore

## How to Run

Install dependencies:
pip install -r requirements.txt

Train the model:
python train_model.py

Run the Flask API:
python app.py

API Endpoint:
POST /predict

Example input:
I love this product

Output:
Positive

## Author

Manshi Singh