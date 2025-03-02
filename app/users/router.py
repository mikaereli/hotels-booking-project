from fastapi import APIRouter, Response
from app.users.auth import authenticate_user, create_access_token, get_password_hash, verify_password
from app.users.dao import UsersDao
from app.exceptions import InccorrectEmailOrPasswordException, UserAlredyExistsException
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)

@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlredyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDao.add(email=user_data.email, hashed_password=hashed_password)

@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise InccorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token