from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserCreate
from app.models.user import User

class UserService:
    @staticmethod
    async def register_user(db: AsyncSession, user_data: UserCreate):
        existing_user = UserRepository.get_user_by_email_or_username(db, user_data.username)
        if existing_user:
            return None #user already exists
        
        new_user = User(
            firstname=user_data.firstname,
            lastname=user_data.lastname,
            username=user_data.username,
            email=user_data.email,
            password=hash_password(user_data.password),
        )
        
        return await UserRepository.create_user(db, new_user)
    
    @staticmethod
    async def authenticate_user(db: AsyncSession, username_or_email: str, password: str):
        user = await UserRepository.get_user_by_email_or_username(db, username_or_email)
        if user and verify_password(password, user.password):
            return create_access_token({"sub": user.username})
        return None