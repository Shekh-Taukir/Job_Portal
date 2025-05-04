from datetime import datetime, timedelta
from fastapi import Depends
from typing import Annotated
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from ..db.db_init import db_dependency
from ..users.model import User
from ..users.exception import UserNotAuthorized
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = str(os.getenv("SECRET_KEY"))
ALGORITHM = str(os.getenv("ALGORITHM"))
TOKEN_TIME = 20

brcryt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def of_authenticate_user(as_username: str, as_password: str, db: db_dependency):
    user = (
        db.query(User)
        .filter((User.email == as_username) & (User.password == as_password))
        .first()
    )

    if not user:
        return False

    return user


def of_create_access_token(as_email: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": as_email, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def of_login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    user = of_authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise UserNotAuthorized()

    token = of_create_access_token(
        str(user.email), user.id, timedelta(minutes=TOKEN_TIME)
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


async def of_get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_email = payload.get("sub")
        user_id = payload.get("id")

        if user_email is None or user_id is None:
            raise UserNotAuthorized()
        return {
            "user_email": user_email,
            "user_id": user_id,
        }

    except JWTError:
        raise UserNotAuthorized()
