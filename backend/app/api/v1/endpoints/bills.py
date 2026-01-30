from fastapi import APIRouter
from typing import List

from app.api.deps import CurrentUser, DBSession
from app.schemas.bill import BillCreate, BillResponse, BillList

router = APIRouter()


@router.get("", response_model=BillList)
async def list_bills(
    current_user: CurrentUser,
    db: DBSession,
    skip: int = 0,
    limit: int = 20,
):
    """List bills for current merchant"""
    # TODO: Implement bill listing
    return BillList(items=[], total=0, skip=skip, limit=limit)


@router.post("", response_model=BillResponse)
async def create_bill(
    bill: BillCreate,
    current_user: CurrentUser,
    db: DBSession,
):
    """Create a new bill"""
    # TODO: Implement bill creation
    return BillResponse(
        id="placeholder",
        merchant_id=current_user.sub,
        customer_id=bill.customer_id,
        bill_number="BILL-0001",
        amount=bill.amount,
        title=bill.title,
        tax_type=bill.tax_type,
        send_type=bill.send_type,
        send_channel=bill.send_channel,
        status="DRAFT",
    )


@router.get("/{bill_id}", response_model=BillResponse)
async def get_bill(
    bill_id: str,
    current_user: CurrentUser,
    db: DBSession,
):
    """Get bill by ID"""
    # TODO: Implement bill retrieval
    return BillResponse(
        id=bill_id,
        merchant_id=current_user.sub,
        customer_id="placeholder",
        bill_number="BILL-0001",
        amount=0,
        title="Placeholder",
        tax_type="TAX",
        send_type="IMMEDIATE",
        send_channel="ALIMTALK",
        status="DRAFT",
    )
