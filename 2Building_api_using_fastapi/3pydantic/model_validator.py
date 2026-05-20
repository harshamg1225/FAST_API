from pydantic import BaseModel, Field, EmailStr, AnyUrl, model_validator
from typing import Dict, List, Annotated


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    email: EmailStr
    married: bool
    allegies: List[str]
    contact_detail: Dict[str, str]

    @model_validator(mode="after")
    def validate_emrgency_contact(self):

        if self.age > 60 and "emergency" not in self.contact_detail:
            raise ValueError("Patients older than 60 must have emrgrency contanct ")

        return self


patient_info = {
    "name": "Harsha",
    "age": "",
    "weight": 34,
    "married": True,
    "allegies": ["pollen", "dust"],
    "contact_detail": {"phone_number": "9199102910"},
    "email": "abc@hdfc.com",
}

patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

    print(patient.weight)
    print(patient.married)
    print(patient.allegies)
    print(patient.contact_detail)
    print(patient.email)
    print("inserted")


insert_patient_data(patient1)
