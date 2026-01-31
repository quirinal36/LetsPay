from fastapi import APIRouter, Depends

from app.core.security import TokenData, get_current_user

router = APIRouter()


@router.get("")
async def list_bills(current_user: TokenData = Depends(get_current_user)):
    return {"bills": [], "total": 0}


@router.post("")
async def create_bill(current_user: TokenData = Depends(get_current_user)):
    return {"message": "Bill creation endpoint - to be implemented"}
