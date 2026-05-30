from pydantic import BaseModel


class User(BaseModel):
    Username: str
    password: str


class UserInDB(User):
    hashed_passoword: str

