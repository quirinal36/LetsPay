from fastapi import APIRouter, Depends

from app.core.security import TokenData, get_current_user

router = APIRouter()


@router.get("")
async def list_customers(current_user: TokenData = Depends(get_current_user)):
    return {"customers": [], "total": 0}


@router.post("")
async def create_customer(current_user: TokenData = Depends(get_current_user)):
    return {"message": "Customer creation endpoint - to be implemented"}
