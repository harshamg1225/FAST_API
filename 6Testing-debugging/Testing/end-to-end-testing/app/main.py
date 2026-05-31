from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Applicant(BaseModel):
    income: float
    age: int
    employment_status: str


@app.post("/loan-eligibility")
def check_eligibility(application: Applicant):

    if (
        application.income > 50000
        and application.age > 21
        and application.employment_status == "Employed"
    ):
        return {"elligibility": True}

    else:
        return {"elligibility": False}
