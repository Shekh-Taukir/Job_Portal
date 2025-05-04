from fastapi import HTTPException


class UserError(HTTPException):
    """Base class for Users related errors"""

    pass


class UserNotFound(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="User data not found")


class LoginEmailError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="User credentials are invalid")


class UserNotAuthorized(UserError):
    def __init__(self):
        super().__init__(status_code=401, detail="Could not validate user")
