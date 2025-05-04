from ...db.db_init import db_dependency
from .email_setup import of_send_email

from sqlalchemy.sql import text
import threading


# function to get the email from the job_apply_id entry
def of_get_user_email_from_jobapply(job_apply_id: int, db: db_dependency):

    sql = text("select user_email, user_name from of_get_user_email(:job_apply_id);")
    result = db.execute(sql, {"job_apply_id": job_apply_id}).fetchone()

    if result:
        user_email = result[0]
        user_name = result[1]
    else:
        user_email = None
        user_name = None
    return {"user_email": user_email, "user_name": user_name}


# function that get user's full name and  email from user_id
def of_get_user_email_from_userid(user_id: int, db: db_dependency):
    from ...users.model import User

    user = db.query(User).filter(User.id == user_id).first()

    return {
        "user_name": f"{user.first_name}, {user.last_name}",  # type: ignore
        "user_email": user.email,  # type: ignore
    }


# function that get job title and company name of the job from job_id
def of_get_job_and_company_name(job_id: int, db: db_dependency):
    sql = text("select job_title, company_name from of_get_job_and_cmpy_name(:job_id);")
    result = db.execute(sql, {"job_id": job_id}).fetchone()

    if result:
        job_title = result[0]
        company_name = result[1]
    else:
        job_title = None
        company_name = None

    return {
        "job_title": job_title,
        "company_name": company_name,
    }


####################### Mail Email Function #######################
# function that process the email functionality to the applicant via gmail_id
def of_process_email(
    as_subject: str,
    as_body: str,
    ai_ref_id: dict,
    db: db_dependency,
    ai_type: int = 1,
):
    """
    ai_type: field that decides that function is called from which api group
    1: job_apply_id - when status of job application gets changed
    2: user_id - when user applys to a new job
    """

    ib_flag = False

    match (ai_type):
        case 1:
            # eg: Hi Taukir, status of your job application has been changed

            job_apply_id = ai_ref_id["job_apply_id"]
            result = of_get_user_email_from_jobapply(job_apply_id, db)
            user_email = result["user_email"]
            user_name = result["user_name"]

            if not user_name:
                user_name = ""
            as_body = as_body.replace("<user_name>", user_name)

        case 2:
            # eg: Taukir, your job application was sent to Google

            user_id, job_id = (
                ai_ref_id["user_id"],
                ai_ref_id["job_id"],
            )

            user_result = of_get_user_email_from_userid(user_id, db)
            user_name, user_email = (
                user_result["user_name"],
                user_result["user_email"],
            )

            job_result = of_get_job_and_company_name(job_id, db)
            job_title, company_name = (
                job_result["job_title"],
                job_result["company_name"],
            )

            as_subject = as_subject.replace("<user_name>", user_name)  # type: ignore
            as_subject = as_subject.replace("<company_name>", company_name)  # type: ignore

            as_body = as_body.replace("<company_name>", company_name)  # type: ignore
            as_body = as_body.replace("<job_title>", job_title)  # type: ignore

    try:
        thrd1 = threading.Thread(
            target=of_send_email, args=(as_subject, as_body, user_email)
        )
        thrd1.start()

    except Exception as e:
        ib_flag = True
        print(e)

    if not ib_flag:
        print("EMail sent")
    else:
        print("Errror in email")
