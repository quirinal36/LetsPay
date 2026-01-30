from datetime import datetime
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from pydantic import BaseModel

from app.core.config import settings

security = HTTPBearer()


class TokenData(BaseModel):
    """Token payload data"""
    sub: str  # user id
    email: Optional[str] = None
    exp: datetime


async def verify_supabase_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> TokenData:
    """Verify Supabase JWT token"""
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            audience="authenticated",
        )

        user_id: str = payload.get("sub")
        email: str = payload.get("email")
        exp: int = payload.get("exp")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing user ID",
            )

        return TokenData(sub=user_id, email=email, exp=datetime.fromtimestamp(exp))

    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}",
        )


async def get_current_user(
    token_data: TokenData = Depends(verify_supabase_token),
) -> TokenData:
    """Get current authenticated user from token"""
    return token_data
