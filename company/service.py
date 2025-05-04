from ..db.db_init import db_dependency
from ..base_code.base_router import of_result_msg, of_update_model
from .model import Company
from .schema import *
from .exception import *


# -> CompanyListModel
def of_get_all_companies(db: db_dependency) -> list[CompanyListModel]:
    lu_company = (
        db.query(Company)
        .filter(Company.isActive == True)
        .order_by(Company.id.desc())
        .all()
    )
    return lu_company  # type:ignore


def of_add_company(db: db_dependency, newCmpy: CompanyAddModel):
    if newCmpy is None:

        raise CompanyNotFound()

    company = Company(
        name=newCmpy.name,
        founder=newCmpy.founder,
        founded_date=newCmpy.founded_date,
        isActive=newCmpy.isActive,
    )

    db.add(company)
    db.commit()
    db.refresh(company)

    return of_result_msg(True, "New Company added", company)


def of_inactive_company(company_id: int, db: db_dependency):
    if company_id <= 0:
        raise CompanyIdError()

    cmpy = db.query(Company).filter(Company.id == company_id).first()

    if cmpy is None:
        raise CompanyNotFound()

    if not cmpy.isActive:  # type:ignore
        return of_result_msg(True, "Company already marked as Inactive")

    cmpy.isActive = False  # type:ignore

    db.commit()
    db.refresh(cmpy)

    return of_result_msg(True, "Company marked as Inactive")


def of_update_company(
    company_id: int, new_cmpy: CompanyAddModel, db: db_dependency
) -> CompanyAddModel:
    if company_id <= 0:
        raise CompanyIdError()

    cmpy = db.query(Company).filter(Company.id == company_id).first()

    if not new_cmpy or not cmpy:
        raise CompanyNotFound()

    of_update_model(cmpy, new_cmpy, True, db)

    return cmpy


def of_validate_company(company_id: int, db: db_dependency):
    if company_id <= 0:
        raise CompanyIdError()

    job = (
        db.query(Company)
        .filter((Company.id == company_id) & (Company.isActive == True))
        .first()
    )

    if job is None:
        return False
    else:
        return True
