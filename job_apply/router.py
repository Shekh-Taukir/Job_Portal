from fastapi import APIRouter
from . import service
from .schema import *
from ..db.db_init import db_dependency

router = APIRouter()


@router.get("/get_user_applies", response_model=list[JobApplyListModel])
async def of_get_user_applies(user_id: int, db: db_dependency):
    return service.of_get_user_applies(user_id, db)


@router.post("/apply_job")
async def of_apply_job(newJobApply: JobApplyModel, db: db_dependency):
    return service.of_apply_job(newJobApply, db)


@router.post("/change_job_status")
async def of_change_job_status(job_status: JobStatusChange, db: db_dependency):
    return service.of_change_job_status(job_status, db)
