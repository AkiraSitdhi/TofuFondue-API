from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict

app = FastAPI()

class Url(BaseModel):
    url: str

class Prediction(BaseModel):
    prediction: list

@app.get("/")
def home():
    return {"Test":"OK"}

@app.post("/predict",response_model=Prediction)
def predict(payload: Url):
    prediction = predict(Url)
    return {"prediction":prediction}


