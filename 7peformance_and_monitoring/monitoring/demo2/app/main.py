from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


app=FastAPI()


Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():

    return {"message":"Fastapi with promethus , grafana, docker"}

@app.get("/ping")
def ping():
    return {"message":"pong"}
