from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql.expression import or_
from app.models.user import User
from app.schemas.user import UserResponse

class UserRepository():
    @staticmethod
    async def get_user_by_email_or_username(db: AsyncSession, username_or_email: str):
        stmt = select(User).where(or_(User.email == username_or_email, User.username == username_or_email))
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def create_user(db: AsyncSession, user: User):
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return UserResponse.model_validate(user)