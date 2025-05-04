from fastapi import APIRouter
from starlette import status
from sqlalchemy.exc import SQLAlchemyError

from ..db.db_init import db_dependency
from .schema import *
from . import service

router = APIRouter()


# response_model=CompanyListModel
# response_model=CompanyResultModel
@router.get(
    "/get_companies",
    response_model=CompanyResultModel,
)
async def of_get_all_companies(db: db_dependency):

    try:
        result = service.of_get_all_companies(db)
        return {"success": True, "result": result}
        # return result
    except SQLAlchemyError as e:
        return {
            "success": False,
            "result": f"Database error: {str(e)}",
        }
        # return service.of_get_all_companies(db)


@router.post("/add_company", status_code=status.HTTP_201_CREATED)
async def of_add_company(db: db_dependency, newCmpy: CompanyAddModel):

    return service.of_add_company(db, newCmpy)


@router.patch("/company_inActive")
async def of_inactive_company(company_id: int, db: db_dependency):

    return service.of_inactive_company(company_id=company_id, db=db)


@router.post("/update_company", response_model=CompanyUpdateModel)
async def of_update_company(
    company_id: int, new_cmpy: CompanyAddModel, db: db_dependency
):

    result = service.of_update_company(company_id, new_cmpy, db)
    return {"success": True, "result": result}
