from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class InputData(BaseModel):
    feature1: float
    feature2: float


@app.get("/home")
def get_home():
    return {"message": "welcome to locust demo"}


@app.post("/predict")
def predict(data: InputData):

    return {"result1": (data.feature1 + data.feature2)}
