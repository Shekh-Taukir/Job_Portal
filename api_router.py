from fastapi import APIRouter
from .company.router import router as company_router
from .jobs.router import router as job_router
from .users.router import router as user_router
from .job_apply.router import router as job_apply_router
from .auth.router import router as auth_router

router = APIRouter()

router.include_router(company_router, prefix="/company", tags=["Company"])
router.include_router(job_router, prefix="/job", tags=["Jobs"])
router.include_router(user_router, prefix="/user", tags=["Users"])
router.include_router(job_apply_router, prefix="/job_apply", tags=["Job Applies"])
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
