from fastapi import APIRouter

# from api.auth.auth import auth_router
from api.machine.machine import machine_router

router = APIRouter()
# router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(machine_router, prefix="/machine", tags=["Machine"])

__all__ = ["router"]
