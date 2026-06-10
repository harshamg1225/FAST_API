from fastapi import FastAPI, HTTPException
from shemas import IrisFlower
import numpy as np

from model import Model


app = FastAPI(
    title="Predicting the Flower cate",
    description="This end point used for predicting flower cate",
)


@app.post("/Predition")
def predict_flower(data: IrisFlower):

    user_input = np.array(
        [[data.SepalLengthCm, data.SepalWidthCm, data.PetalLengthCm, data.PetalWidthCm]]
    )

    
    output = Model.predict(user_input)
    print(type(output), output)

    return {"predicted": int(output[0])}
