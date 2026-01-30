from fastapi import APIRouter

from app.api.deps import CurrentUser, DBSession
from app.schemas.customer import CustomerCreate, CustomerResponse, CustomerList

router = APIRouter()


@router.get("", response_model=CustomerList)
async def list_customers(
    current_user: CurrentUser,
    db: DBSession,
    skip: int = 0,
    limit: int = 20,
):
    """List customers for current merchant"""
    return CustomerList(items=[], total=0, skip=skip, limit=limit)


@router.post("", response_model=CustomerResponse)
async def create_customer(
    customer: CustomerCreate,
    current_user: CurrentUser,
    db: DBSession,
):
    """Create a new customer"""
    return CustomerResponse(
        id="placeholder",
        merchant_id=current_user.sub,
        name=customer.name,
        phone=customer.phone,
        email=customer.email,
    )


@router.get("/{customer_id}", response_model=CustomerResponse)
async def get_customer(
    customer_id: str,
    current_user: CurrentUser,
    db: DBSession,
):
    """Get customer by ID"""
    return CustomerResponse(
        id=customer_id,
        merchant_id=current_user.sub,
        name="Placeholder",
        phone="010-0000-0000",
    )
