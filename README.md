# Task Priority ML API

This project provides a simple **FastAPI** application that predicts the priority of a task based on its description.  

---

## Project Structure

- `main.py` — FastAPI application that serves the prediction endpoint.  
- `train_model.py` — script to train the model using `tasks.csv` dataset and save it as `model.pkl`.  
- `tasks.csv` — dataset with sample tasks and their priorities.  
- `test_api.py` — unit tests for the API.  
- `requirements.txt` — required dependencies.  

---

## Installation & Usage

1. Clone the repository
   ```
   git clone https://github.com/d-komissarchik/todo-api.git
   cd todo-api
   ```
2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
3. **Train the model (this generates model.pkl)**:
   ```
   python train_model.py
   ```
4. **Run the FastAPI server**:
   ```
   uvicorn main:app --reload
   ```
5. **Access the API documentation at**:
   http://127.0.0.1:8000/docs
  
---

## API Endpoint
POST `/predict`

Request body:
```
{
  "task_description": "Fix login bug on website"
}
```
Response:
```
{
  "predicted_priority": "high"
}
```