import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

# Load database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an async engine to connect to the existing database
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session factory
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

# Define base class for models
Base = declarative_base()

# Dependency to get database session
async def get_db():
    async with SessionLocal() as session:
        yield session