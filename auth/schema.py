from pydantic import BaseModel


class CreatedUserRequest(BaseModel):
    user_email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
