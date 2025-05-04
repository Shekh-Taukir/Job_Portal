from fastapi import APIRouter

from .schema import JobsModel, JobListResult
from ..db.db_init import db_dependency
from . import service
from ..job_apply.schema import JobApplyListModel

router = APIRouter()


@router.get("/all_active_jobs", response_model=JobListResult)
async def of_get_all_jobs(db: db_dependency):
    jobs = service.of_get_all_jobs(db)

    return {"success": True, "result": jobs}


@router.get("/company_jobs", response_model=JobListResult)
async def of_get_company_jobs(company_id: int, db: db_dependency):

    jobs = service.of_get_company_jobs(db, company_id)
    return {"success": True, "result": jobs}


@router.post("/add_job")
async def of_add_job(company_id: int, newJob: JobsModel, db: db_dependency):
    return service.of_add_job(company_id, newJob, db)


@router.patch("/job_inactive")
async def of_inactive_job(job_id: int, db: db_dependency):
    return service.of_inactive_job(job_id, db)


@router.post("/job_update")
async def of_job_update(job_id: int, newJob: JobsModel, db: db_dependency):
    return service.of_job_update(job_id, newJob, db)


@router.get("/job_applicants", response_model=list[JobApplyListModel])
async def of_get_applicants(job_id: int, db: db_dependency):
    return service.of_get_applicants(job_id, db)
