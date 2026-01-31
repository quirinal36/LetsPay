from fastapi import APIRouter

from app.api.v1.endpoints import auth, bills, customers, payments

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(bills.router, prefix="/bills", tags=["bills"])
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
