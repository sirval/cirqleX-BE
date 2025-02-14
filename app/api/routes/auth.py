from fastapi import APIRouter
from schemas.auth import RegistrationBase

router = APIRouter(
    prefix= 'auth',
    tags=['Authentication']
)

@router.post('/register')
def register(request: RegistrationBase):
    pass

