from pydantic import BaseModel
from datetime import date


class CompanyBaseModel(BaseModel):
    name: str
    founder: str
    founded_date: date
    isActive: bool


class CompanyAddModel(CompanyBaseModel):
    pass


class CompanyListModel(CompanyBaseModel):
    id: int

    class Config:
        orm_mode = True


class CompanyResultModel(BaseModel):
    success: bool
    result: list[CompanyListModel]

    # class Config:
    #     orm_mode = True


class CompanyUpdateModel(BaseModel):
    success: bool
    result: CompanyListModel
