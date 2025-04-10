from fastapi import APIRouter

from api.v1.endpoints.reservation import router as reservation_router
from api.v1.endpoints.table import router as table_router

router = APIRouter()
router.include_router(reservation_router)
router.include_router(table_router)
