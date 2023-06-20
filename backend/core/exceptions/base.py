from http import HTTPStatus


class CustomException(Exception):
    code = HTTPStatus.BAD_REQUEST
    success = False
    message = HTTPStatus.BAD_REQUEST.description

    def __init__(self, code=0, message=None):
        if code:
            self.code = code
        if message:
            self.message = message

class BadRequestException(CustomException):
    code = HTTPStatus.BAD_REQUEST
    success = False
    message = HTTPStatus.BAD_REQUEST.description

class UnauthorizedException(CustomException):
    code = HTTPStatus.UNAUTHORIZED
    success = False
    message = HTTPStatus.UNAUTHORIZED.description

class PaymentRequiredException(CustomException):
    code = HTTPStatus.PAYMENT_REQUIRED
    success = False
    message = HTTPStatus.PAYMENT_REQUIRED.description

class ForbiddenException(CustomException):
    code = HTTPStatus.FORBIDDEN
    success = False
    message = HTTPStatus.FORBIDDEN.description

class NotFoundException(CustomException):
    code = HTTPStatus.NOT_FOUND
    success = False
    message = HTTPStatus.NOT_FOUND.description
    
class MethodNotAllowedException(CustomException):
    code = HTTPStatus.METHOD_NOT_ALLOWED
    success = False
    message = HTTPStatus.METHOD_NOT_ALLOWED.description
   
class NotAcceptableException(CustomException):
    code = HTTPStatus.NOT_ACCEPTABLE
    success = False
    message = HTTPStatus.NOT_ACCEPTABLE.description
   
class ProxyAuthenticationRequiredException(CustomException):
    code = HTTPStatus.PROXY_AUTHENTICATION_REQUIRED
    success = False
    message = HTTPStatus.PROXY_AUTHENTICATION_REQUIRED.description
   
class RequestTimeOutException(CustomException):
    code = HTTPStatus.REQUEST_TIMEOUT
    success = False
    message = HTTPStatus.REQUEST_TIMEOUT.description
   
class ConflictException(CustomException):
    code = HTTPStatus.CONFLICT
    success = False
    message = HTTPStatus.CONFLICT.description

class GoneException(CustomException):
    code = HTTPStatus.GONE
    success = False
    message = HTTPStatus.GONE.description

class PreconditionFailedException(CustomException):
    code = HTTPStatus.PRECONDITION_FAILED
    success = False
    message = HTTPStatus.PRECONDITION_FAILED.description

class UriTooLongException(CustomException):
    code = HTTPStatus.REQUEST_URI_TOO_LONG
    success = False
    message = HTTPStatus.REQUEST_URI_TOO_LONG.description

class UnsupportedMediaTypeException(CustomException):
    code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    success = False
    message = HTTPStatus.UNSUPPORTED_MEDIA_TYPE.description

class RangeNotSatisfiableException(CustomException):
    code = HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE
    success = False
    message = HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE.description

class LockedException(CustomException):
    code = HTTPStatus.LOCKED
    success = False
    message = HTTPStatus.LOCKED.description

class UpgradeRequiredException(CustomException):
    code = HTTPStatus.UPGRADE_REQUIRED
    success = False
    message = HTTPStatus.UPGRADE_REQUIRED.description

class TooManyRequestsException(CustomException):
    code = HTTPStatus.TOO_MANY_REQUESTS
    success = False
    message = HTTPStatus.TOO_MANY_REQUESTS.description

class UnavailableForLegalReasonsException(CustomException):
    code = HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS
    success = False
    message = HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS.description

class UnprocessableEntity(CustomException):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    success = False
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description

class DuplicateValueException(CustomException):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    success = False
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description
