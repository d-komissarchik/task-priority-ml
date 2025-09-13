import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv("tasks.csv")

X = data["task_description"]
y = data["priority"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])


model.fit(X, y)

joblib.dump(model, "model.pkl")

print("The model was trained and saved as model.pkl")