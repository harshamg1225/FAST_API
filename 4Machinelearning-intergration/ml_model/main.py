from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, Batch_prediction


app = FastAPI()


@app.get("/")
def index():
    return {"Message": "Welcome to the ML model prediction"}


@app.post("/Prediction", response_model=OutputSchema)
def Predict(user_input: InputSchema):

    prediction = make_prediction(user_input.model_dump())

    return OutputSchema(Price=prediction)


@app.post("/Batch_prediction", response_model=list[OutputSchema])
def BatchPredict(user_input: list[InputSchema]):

    prediction = Batch_prediction([x.model_dump() for x in user_input])

    return [OutputSchema(Price=i) for i in prediction]
