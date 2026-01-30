from fastapi import APIRouter

from app.api.deps import CurrentUser, DBSession
from app.schemas.payment import PaymentResponse, PaymentList

router = APIRouter()


@router.get("/history", response_model=PaymentList)
async def list_payments(
    current_user: CurrentUser,
    db: DBSession,
    skip: int = 0,
    limit: int = 20,
):
    """List payment history"""
    return PaymentList(items=[], total=0, skip=skip, limit=limit)


@router.get("/bill/{bill_id}", response_model=PaymentResponse)
async def get_payment_for_bill(
    bill_id: str,
    db: DBSession,
):
    """Get payment page data for a bill (public endpoint for customers)"""
    return PaymentResponse(
        id="placeholder",
        bill_id=bill_id,
        amount=0,
        status="PENDING",
    )
