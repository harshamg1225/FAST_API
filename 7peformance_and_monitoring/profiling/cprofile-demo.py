import cProfile
import os
import time
from fastapi import FastAPI, Request
import datetime
from fastapi.responses import JSONResponse


PROFILE_DIR = "Profiles"

os.makedirs(PROFILE_DIR, exist_ok=True)


app = FastAPI()


@app.middleware("http")
async def create_profile(request: Request, call_next):

    # as we know cpfile will create file (for that we are creating folder and naming for the file)
    time_stamp = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")

    path = request.url.path.strip("/").replace("/", "_") or "root"

    profile_name = os.path.join(PROFILE_DIR, f"{path}_{time_stamp}.prof")

    profiler = cProfile.Profile()

    profiler.enable()

    response = await call_next(request)
    profiler.dump_stats(profile_name)

    profiler.disable()

    print(f"Profiling saved: {profile_name}")
    return response


@app.get("/")
async def root():
    return {"home": "welcome"}


@app.get("/compute")
async def compute():
    time.sleep(1)
    result = sum(i**2 for i in range(10000))

    return JSONResponse({"result": result})
