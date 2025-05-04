from pydantic import BaseModel
from datetime import datetime


class JobApplyModel(BaseModel):
    job_id: int
    user_id: int


class JobApplyListModel(BaseModel):

    job_apply_id: int
    job_title: str
    user_name: str
    status_desc: str
    applied_date: datetime

    class Config:
        orm_mode = True


class JobStatusChange(BaseModel):
    job_apply_id: int
    status_id: int
