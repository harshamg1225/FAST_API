from fastapi import FastAPI, Depends

app = FastAPI()


# dependency functions
def get_db():

    db = {"connections": "mock_db_connection"}
    try:
        yield db

    finally:
        db.close()


# end point


@app.get("/home")
def home(db=Depends(get_db)):
    return {"db_status": db["connections"]}
