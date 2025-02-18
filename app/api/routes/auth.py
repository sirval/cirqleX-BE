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

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    created_user = await UserService.register_user(db, user)
    if not created_user:
        raise_error(400, 'User already exists')
    return format_response(201, 'success', 'Request successful', created_user)

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    token = await UserService.authenticate_user(db, request.username_or_email, request.password)
    if not token:
        raise_error(401, 'Invalid credentials')
    return format_response(200, 'success', 'Request successful', TokenResponse(access_token=token))


