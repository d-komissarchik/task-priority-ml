from fastapi import FastAPI
from pydantic import BaseModel
import joblib


model = joblib.load("model.pkl")

app = FastAPI(title="Task Priority ML API", version="1.0.0")

class TaskRequest(BaseModel):
    task_description: str

class TaskResponse(BaseModel):
    predicted_priority: str

@app.post("/predict", response_model=TaskResponse)
def predict_priority(request: TaskRequest):
    prediction = model.predict([request.task_description])[0]
    return TaskResponse(predicted_priority=prediction)

