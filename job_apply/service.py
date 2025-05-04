from sqlalchemy.sql import text
from ..db.db_init import db_dependency

from .schema import *
from .model import Job_Apply, Status
from .exception import *

from ..users.exception import UserNotFound
from ..users.service import of_validate_user

from ..jobs.service import of_validate_job

from ..base_code.base_router import of_result_msg
from ..utilities.email import service as email_service

####################### Functions to validate values #######################


# function to validate the status_id
def of_validate_status(status_id: int, db: db_dependency) -> bool:
    if status_id <= 0:
        raise StatusNotFound()

    status = db.query(Status).filter(Status.id == status_id).first()

    if not status:
        return False
    return True


# function to validate the new job_apply detail is valid or not
def of_validate_jobApply(job_apply: JobApplyModel, db: db_dependency):

    user_id = job_apply.user_id
    job_id = job_apply.job_id
    lb_flag = False

    if of_validate_user(user_id, db) and of_validate_job(job_id, db):
        lb_flag = True

    if lb_flag:
        job_apply = (
            db.query(Job_Apply)
            .filter((Job_Apply.user_id == user_id) & (Job_Apply.job_id == job_id))
            .first()
        )
    if job_apply or not lb_flag:
        return False


# function to validate the job_apply_id
def of_validate_job_apply_id(job_apply_id: int, db: db_dependency) -> bool:
    if job_apply_id <= 0:
        raise JobApplyNotFound()
    job_apply = db.query(Job_Apply).filter(Job_Apply.id == job_apply_id).first()

    if not job_apply:
        return False
    return True


####################### Functions to serve API response #######################


# function to get the job applies for specific user
def of_get_user_applies(user_id: int, db: db_dependency) -> list[JobApplyListModel]:

    if not of_validate_user(user_id, db):
        raise UserNotFound()

    job_applies = (
        db.execute(
            text("select * from of_get_job_apply_per_user(:user_id, :id_type)"),
            {"user_id": user_id, "id_type": 1},
        )
        .mappings()
        .all()
    )
    return job_applies  # type:ignore


# function to apply to a job for the following user
def of_apply_job(newJobApply: JobApplyModel, db: db_dependency):

    if newJobApply is None:
        raise JobApplyNotFound()

    if not of_validate_jobApply(newJobApply, db):
        raise JobApplyNotFound()

    job_Apply = Job_Apply(
        user_id=newJobApply.user_id,
        job_id=newJobApply.job_id,
        status_id=1,
    )

    db.add(job_Apply)
    db.commit()
    db.refresh(job_Apply)

    arg_id = {
        "user_id": newJobApply.user_id,
        "job_id": newJobApply.job_id,
    }

    email_service.of_process_email(
        "<user_name>, your application was sent to <company_name>",
        "Your application has sent to <company_name> for <job_title>",
        arg_id,
        db,
        2,
    )

    return job_Apply


# function to change the status of the job apply entry
def of_change_job_status(job_status: JobStatusChange, db: db_dependency):

    job_apply_id = job_status.job_apply_id
    status_id = job_status.status_id

    if not of_validate_job_apply_id(job_apply_id, db):
        raise JobApplyNotFound()

    if not of_validate_status(status_id, db):
        raise StatusNotFound()

    job_apply = db.query(Job_Apply).filter(Job_Apply.id == job_apply_id).first()

    if not job_apply:
        raise JobApplyNotFound()

    job_apply.status_id = status_id  # type:ignore
    db.commit()
    db.refresh(job_apply)

    email_service.of_process_email(
        "Status of your job application has changed",
        "Hi <user_name>, Status of your job application has been updated.",
        {"job_apply_id": job_apply_id},
        db,
        1,
    )

    return of_result_msg(True, "Job Status has been changed", job_apply)
