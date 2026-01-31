from fastapi import APIRouter, Depends

from app.core.security import TokenData, get_current_user

router = APIRouter()


@router.get("/me")
async def get_me(current_user: TokenData = Depends(get_current_user)):
    return {"user_id": current_user.sub, "email": current_user.email}
