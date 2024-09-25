from fastapi import APIRouter

from supermarket_service.routers import fruits_router

router = APIRouter()

router.include_router(fruits_router.router, prefix="/fruits")