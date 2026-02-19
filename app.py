from fastapi import FastAPI
from model import predict

# create API app
app = FastAPI()

# home route
@app.get("/")
def home():
    return {"message": "AI API running"}

# prediction route
@app.get("/predict")
def get_prediction(text: str):
    result = predict(text)
    return result
