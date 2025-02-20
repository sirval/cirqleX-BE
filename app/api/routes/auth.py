from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import LoginRequest, TokenResponse
from app.core.config import get_db
from app.utils.response import format_response, raise_error

router = APIRouter(
    prefix= '/auth',
    tags=['Authentication']
)

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        created_user = await UserService.register_user(db, user)
        user_data = {**created_user.model_dump(), "date_joined": created_user.date_joined.strftime("%b. %d, %Y")}
        return format_response(201, 'success', 'User registered successfully', user_data)
    except Exception as e:
        raise_error(400, str(e))
    except Exception as e:
        raise_error(500, 'A server error occurred')

@router.post("/login")
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    token = await UserService.authenticate_user(db, request.username_or_email, request.password)
    if not token:
        raise_error(401, 'Invalid credentials')
    return format_response(200, 'success', 'Request successful', token)


