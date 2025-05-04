from .model import Jobs
from .schema import *
from .exception import *
from ..company.exception import CompanyIdError
from ..db.db_init import db_dependency
from ..base_code.base_router import of_result_msg, of_update_model
from ..company.service import of_validate_company


####################### Functions to serve API response #######################
def of_get_all_jobs(db: db_dependency, company_id: int = 0) -> list[JobResponseModel]:
    jobs_query = db.query(Jobs).filter(Jobs.isActive == True).order_by(Jobs.id.desc())

    if company_id > 0:
        jobs_query = jobs_query.filter(Jobs.company == company_id)

    return jobs_query.all()  # type:ignore


def of_get_company_jobs(db: db_dependency, company_id: int) -> list[JobResponseModel]:

    if company_id <= 0:
        raise CompanyIdError()

    return of_get_all_jobs(db, company_id)


def of_add_job(company_id: int, newJob: JobsModel, db: db_dependency):

    if not of_validate_company(company_id, db):
        raise CompanyIdError()

    if newJob is None:
        raise JobNotFound()

    job = Jobs(
        title=newJob.title,
        description=newJob.description,
        posted_date=newJob.posted_date,
        isActive=newJob.isActive,
        company=company_id,
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return of_result_msg(True, None, job)


def of_inactive_job(job_id: int, db: db_dependency):
    if job_id <= 0:
        raise JobIdError()

    job = db.query(Jobs).filter(Jobs.id == job_id).first()

    if job is None:
        raise JobNotFound()

    if not job.isActive:  # type:ignore
        return of_result_msg(True, "Job is already marked as Inactive")
    else:
        job.isActive = bool(False)  # type:ignore
        db.commit()
        db.refresh(job)

        return of_result_msg(True, "Job is marked as Inactive")


def of_job_update(job_id: int, newJob: JobsModel, db: db_dependency):

    if job_id <= 0:
        raise JobIdError()

    job = db.query(Jobs).filter(Jobs.id == job_id).first()

    if newJob is None or job is None:
        raise JobNotFound()

    of_update_model(job, newJob, True, db)

    return of_result_msg(True, None, job)


def of_get_applicants(job_id: int, db: db_dependency):
    if job_id <= 0:
        raise JobNotFound()

    from sqlalchemy.sql import text

    job_applicants = (
        db.execute(
            text("select * from of_get_job_apply_per_user(:job_id, :id_type)"),
            {"job_id": job_id, "id_type": 2},
        )
        .mappings()
        .all()
    )
    return job_applicants


####################### Functions to validate values #######################
def of_validate_job(job_id: int, db: db_dependency) -> bool:

    if job_id <= 0:
        raise JobIdError()

    job = db.query(Jobs).filter(Jobs.id == job_id).first()

    if job is not None:
        return True
    else:
        return False
