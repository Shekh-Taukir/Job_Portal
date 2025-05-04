from .model import User
from .schema import *
from .exception import *
from ..db.db_init import db_dependency
from ..base_code.base_router import of_result_msg


def of_validate_user(user_id: int, db: db_dependency):
    if user_id <= 0:
        raise UserNotFound()

    user = db.query(User).filter(User.id == user_id).first()

    if user is not None:
        return True
    else:
        return False


def of_validate_email(email_id: str, db: db_dependency):
    if email_id is None:
        raise LoginEmailError()

    user = db.query(User).filter(User.email == email_id).first()

    if user is None:
        return True
    else:
        return False


def of_signup_user(newUser: UsersInputModel, db: db_dependency):
    if newUser is None:
        raise UserNotFound()

    if not of_validate_email(newUser.email, db):
        return of_result_msg(False, "Email already exists!!!")

    user = User(
        first_name=newUser.first_name,
        last_name=newUser.last_name,
        email=newUser.email,
        password=newUser.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return of_result_msg(True, None, user)


def of_login_user(loginUser: UserLoginModel, db: db_dependency):

    if loginUser is None:
        raise UserNotFound()

    user = (
        db.query(User)
        .filter((User.email == loginUser.email) & (User.password == loginUser.password))
        .first()
    )

    if user is None:
        return of_result_msg(False, "User Credentials is invalid")

    else:
        return of_result_msg(True, None, [user.id])
