from fastapi import APIRouter

from .schema import *
from . import service
from ..db.db_init import db_dependency


router = APIRouter()


@router.post("/signup_user")
def of_signup_user(newUser: UsersInputModel, db: db_dependency):
    return service.of_signup_user(newUser, db)


@router.post("/login_user")
def of_login_user(login_user: UserLoginModel, db: db_dependency):
    return service.of_login_user(login_user, db)
