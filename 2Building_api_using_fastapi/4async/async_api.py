import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/wait")
async def wait():

    await asyncio.sleep(3)  # non blocking sleep

    return {"Message": "Finished waiting"}
