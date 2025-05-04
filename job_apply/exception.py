from fastapi import HTTPException


####################### JOb Error #######################
class JobApplyError(HTTPException):
    """Base class for job applies related error"""

    pass


class JobApplyNotFound(JobApplyError):

    def __init__(self):
        super().__init__(status_code=400, detail="Job Apply data not found")


####################### Status Error #######################
class StatusError(HTTPException):
    """Base class for Status related errors"""

    pass


class StatusNotFound(StatusError):
    def __init__(self):
        super().__init__(status_code=400, detail="Status data not found")
