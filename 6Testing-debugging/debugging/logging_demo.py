import logging

from fastapi import FastAPI


app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] (line %(lineno)d- %(levelname)s- %(message)s)",
    datefmt="%m-%Y-%d %H:%M:%S",
)


@app.get("/debug")
def debug_route():
    logging.info("Debug end point hit")
    return {"message": "check logs"}
