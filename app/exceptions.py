from fastapi import HTTPException, status

class ExceptionBase(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Something went wrong"
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)



class UserAlredyExistsException(ExceptionBase): 
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class InccorrectEmailOrPasswordException(ExceptionBase):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"


class TokerExpiredException(ExceptionBase):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired"
    

class TokenAbsentException(ExceptionBase):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token absent"
    

class IncorrectTokenFormatException(ExceptionBase):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class UserNotFoundException(ExceptionBase):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User not found"
    