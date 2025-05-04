from fastapi import HTTPException


class CompanyError(HTTPException):
    """Base class for company-related errors"""

    pass


class CompanyNotFound(CompanyError):
    def __init__(self) -> None:
        super().__init__(status_code=204, detail="No company data found")


class CompanyIdError(CompanyError):
    def __init__(self) -> None:
        super().__init__(status_code=400, detail="Company id is not proper")
