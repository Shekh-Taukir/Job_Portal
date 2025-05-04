from fastapi import FastAPI

from .api_router import router as main_router

# create the app
app = FastAPI(title="Jobs4You")

app.include_router(main_router, prefix="/api/v1")

# create the required tables
# Base.metadata.create_all(bind=engine)
