from fastapi import Depends, Request
from jose import jwt, JWTError
from app.config import settings
from app.users.dao import UsersDao
from app.exceptions import IncorrectTokenFormatException, TokenAbsentException, UserNotFoundException

def get_token(request: Request) -> str:
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token 

async def get_current_user(token: str = Depends(get_token)): 
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        print("payload: {}".format(payload.keys()))
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserNotFoundException
    user = await UsersDao.find_one_or_none(id=int(user_id))
    if not user:
        raise UserNotFoundException
    return user
