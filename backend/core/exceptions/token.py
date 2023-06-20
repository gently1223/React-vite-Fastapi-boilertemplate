from core.exceptions import CustomException


class DecodeTokenException(CustomException):
    code = 400
    success = False
    message = "Token decode error"


class ExpiredTokenException(CustomException):
    code = 400
    success = False
    message = "Expired token"
