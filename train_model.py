import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv("sentiment_dataset.csv")

X = data["text"]
y = data["sentiment"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])


# Train model
model.fit(X_train, y_train)


# Test accuracy
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)


# Save model
with open("sentiment_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")