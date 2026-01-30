from fastapi import APIRouter

from app.api.deps import CurrentUser
from app.schemas.auth import UserResponse

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: CurrentUser):
    """Get current user information"""
    return UserResponse(
        id=current_user.sub,
        email=current_user.email or "",
    )
