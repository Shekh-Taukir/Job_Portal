from pydantic import BaseModel


class UsersInputModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UserLoginModel(BaseModel):
    email: str
    password: str
