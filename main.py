from fastapi import FastAPI
from src.api.api import router as api_router


app = FastAPI(
    title="ShelterCare",
    version="1.0",
    docs="/docs"
)
app.include_router(api_router)
