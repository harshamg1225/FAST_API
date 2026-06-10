import time
import logging
from fastapi import FastAPI, Request


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] (line %(lineno)d) - %(levelname)s- %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S",
)


logger = logging.getLogger("Profiler")

app = FastAPI()


@app.middleware("http")
async def add_timing(request: Request, call_next):
    start = time.time()

    response = await call_next(request)
    time_taken = time.time() - start

    logger.info(f" request to {request.url.path} took {time_taken:.3f} second")
    return response


@app.get("/")
def home():

    return {"Message": "Profiling demo"}


@app.get("/slow")
async def slow_endpoint():

    time.sleep(2)
    return {"message": "This is slow endpoint"}


@app.get("/fast")
async def fast_endpoint():

    return {"message": "fast end point"}
