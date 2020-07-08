from fastapi import APIRouter
from .endpoints.authenticaion import router as auth_router

router = APIRouter()

router.include_router(auth_router)
