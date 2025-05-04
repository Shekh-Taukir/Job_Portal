from pydantic import BaseModel
from datetime import date


class JobsModel(BaseModel):
    title: str
    description: str
    posted_date: date
    isActive: bool


class JobResponseModel(JobsModel):
    id: int
    company_name: str

    class config:
        orm_mode = True


class JobListResult(BaseModel):
    success: bool
    result: list[JobResponseModel]
