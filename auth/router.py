from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from ..db.db_init import db_dependency
from .schema import Token
from . import service
from .auth_dependency import auth_dependency
from ..users.exception import UserNotAuthorized

router = APIRouter()


@router.post("/token", response_model=Token)
async def of_login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    return service.of_login_for_access_token(form_data, db)


@router.get("/get_user")
async def of_login_user(user: auth_dependency, db: db_dependency):
    if user is None:
        raise UserNotAuthorized()

    return {"User": user}
