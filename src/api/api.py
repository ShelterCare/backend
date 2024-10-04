from fastapi import APIRouter
from .endpoint.v1 import test

router = APIRouter()
router.include_router(test.router, prefix="/test", tags=["test"])
