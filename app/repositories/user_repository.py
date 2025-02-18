from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User

class UserRepository():
    @staticmethod
    async def get_user_by_email_or_username(db: AsyncSession, username_or_email: str):
        stmt = select(User).where((User.email == username_or_email) | (User.username == username_or_email))
        result = await db.execute(stmt)
        return result.scalar_one_or_none
    
    @staticmethod
    async def create_user(db: AsyncSession, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user