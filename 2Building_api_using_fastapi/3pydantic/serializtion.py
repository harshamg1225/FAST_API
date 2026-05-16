from pydantic import BaseModel


from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address


address_dict = {"city": "kol", "state": "kar", "pin": "571440"}
address1 = Address(**address_dict)


Patient_detail = {"name": "Harsha", "age": 34, "gender": "Male", "address": address1}

patient_info = Patient(**Patient_detail)


temp = patient_info.model_dump(
    include=["name", "age"],
)
print(temp, type(temp))

temp_json = patient_info.model_dump_json(exclude=["name", "age"])

print(temp_json, type(temp_json))
