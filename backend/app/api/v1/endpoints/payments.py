from fastapi import APIRouter, Depends

from app.core.security import TokenData, get_current_user

router = APIRouter()


@router.get("/history")
async def payment_history(current_user: TokenData = Depends(get_current_user)):
    return {"payments": [], "total": 0}
