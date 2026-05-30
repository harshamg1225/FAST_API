import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()


class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        response = await call_next(request)

        duration = time.time() - start_time

        print(f"Request:{request.url.path} processed in {duration:.5f} sec")
        return response


app.add_middleware(TimerMiddleware)


# endpoint


@app.get("/Home")
async def get_method():

    for _ in range(10000000):
        pass

    return {"Message": "Hello world!"}
