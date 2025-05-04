from fastapi import HTTPException


class JobError(HTTPException):
    """Base class for job related errors"""

    pass


class JobNotFound(JobError):

    def __init__(self):
        super().__init__(status_code=204, detail="No job data found")


class JobIdError(JobError):

    def __init__(self):
        super().__init__(status_code=400, detail="Job id is not proper")
