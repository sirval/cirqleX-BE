from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)
    date_joined = Column(DateTime(timezone=True), server_default=func.now())
