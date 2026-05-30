from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


fake_user_db = {
    "johndoe": {"username": "johndoe", "hashed_passowrd": pwd_context.hash("secret123")}
}


def get_user(username: str):

    user = fake_user_db.get(username)
    return user


def verify_passowrd(plain_password, hashed_password):

    return pwd_context.verify(plain_passoword, hashed_password)
