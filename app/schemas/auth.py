from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timezone

class RegistrationBase(BaseModel):
    firstname: str = Field(..., min_length=2, max_length=50)
    lastname: str = Field(..., min_length=2, max_length=50)
    username: str = Field(..., min_length=3, max_length=30, regex="^[a-zA-Z0-9_.-]+$")
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8, max_length=128)
    confirm_password: str = Field(..., min_length=8, max_length=128)
    date_joined: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
