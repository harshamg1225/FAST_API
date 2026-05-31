from fastapi import FastAPI
from app.logic import is_eligible_for_loan
from pydantic import BaseModel


app = FastAPI()


class Applicant(BaseModel):
    income: float
    age: int
    employment_status: str


@app.post("/loan_eligibility")
def loan_eligibilty(applicant: Applicant):

    eligibility = is_eligible_for_loan(
        applicant.income, applicant.age, applicant.employment_status
    )

    return {"eligibility": eligibility}
