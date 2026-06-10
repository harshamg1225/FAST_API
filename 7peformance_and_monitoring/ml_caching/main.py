from fastapi import FastAPI
from model import Model
from shemas import IrisFlower
import redis
import hashlib
import json

app = FastAPI()

redis_client = redis.Redis(host="localhost", port=6379, db=0)


@app.post("/Predict")
async def predict(data: IrisFlower):

    key = data.cache_key()

    cached_result = redis_client.get(key)

    if cached_result:
        print("Serving prediction from cache")

        return json.loads(cached_result)

    prediction = Model.predict([data.to_list()])[0]

    result = {"prediction": int(prediction)}

    redis_client.set(key, json.dumps(result), ex=3600)

    return result
