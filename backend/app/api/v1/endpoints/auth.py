from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db
from app.core.security import TokenData, get_current_user
from app.schemas.auth import (
    SignupRequest,
    SignupResponse,
    UserResponse,
    CheckEmailRequest,
    CheckEmailResponse,
)
from app.models.merchant import Merchant

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: TokenData = Depends(get_current_user)):
    """Get current authenticated user info"""
    return UserResponse(user_id=current_user.sub, email=current_user.email)


@router.post("/signup", response_model=SignupResponse, status_code=status.HTTP_201_CREATED)
async def signup(
    request: SignupRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Register additional business information after Supabase auth signup.
    This endpoint is called after the user signs up via Supabase Auth.
    """
    from sqlalchemy import select

    # Check if email already exists
    result = await db.execute(
        select(Merchant).where(Merchant.email == request.email)
    )
    existing_merchant = result.scalar_one_or_none()

    if existing_merchant:
        # Update existing merchant record (created by auth trigger)
        existing_merchant.phone = request.phone
        existing_merchant.business_name = request.business_name
        if request.business_number:
            existing_merchant.business_number = request.business_number
        if request.representative_name:
            existing_merchant.representative_name = request.representative_name
        existing_merchant.status = "PENDING"

        await db.commit()
        await db.refresh(existing_merchant)

        return SignupResponse(
            success=True,
            message="사업자 정보가 업데이트되었습니다.",
            merchant_id=str(existing_merchant.id),
        )

    # Create new merchant if not exists (fallback)
    new_merchant = Merchant(
        email=request.email,
        phone=request.phone,
        business_name=request.business_name,
        business_number=request.business_number or "",
        representative_name=request.representative_name or "",
        status="PENDING",
    )

    if request.supabase_user_id:
        new_merchant.auth_user_id = request.supabase_user_id

    db.add(new_merchant)
    await db.commit()
    await db.refresh(new_merchant)

    return SignupResponse(
        success=True,
        message="회원가입이 완료되었습니다.",
        merchant_id=str(new_merchant.id),
    )


@router.post("/check-email", response_model=CheckEmailResponse)
async def check_email(
    request: CheckEmailRequest,
    db: AsyncSession = Depends(get_db),
) -> CheckEmailResponse:
    """Check if email is already registered"""
    from sqlalchemy import select

    result = await db.execute(
        select(Merchant).where(Merchant.email == request.email)
    )
    existing = result.scalar_one_or_none()

    return CheckEmailResponse(available=existing is None)
