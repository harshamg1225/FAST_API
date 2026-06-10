import time
from fastapi import FastAPI


app = FastAPI()


@profile
def compuation(n: int):

    result = 0
    for i in range(n):
        result = result + i**2
    time.sleep(1)
    return result


@profile
def process_data(x: int):
    return compuation(x)


@app.get("/profiling")
def profiling(a: int):
    return {"result": process_data(a)}
