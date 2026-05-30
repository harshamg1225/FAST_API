from fastapi import FastAPI
from starlette.middleware.gzip import GzipMiddleware


app = FastAPI()


app.add_middleware(GzipMiddleware, minimum_size=1000)
