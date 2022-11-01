class BaseException(Exception):
    def __init__(self, message, status_code):
        self.status_code = status_code
        super().__init__(message)


class BadRequestException(BaseException):
    def __init__(self, message):
        super().__init__(message, 400)


class UnauthorizedException(BaseException):
    def __init__(self, message):
        super().__init__(message, 401)


class ForbiddenException(BaseException):
    def __init__(self, message):
        super().__init__(message, 403)


class NotFoundException(BaseException):
    def __init__(self, message):
        super().__init__(message, 404)


class MethodNotAllowedException(BaseException):
    def __init__(self, message):
        super().__init__(message, 405)


class ConflictException(BaseException):
    def __init__(self, message):
        super().__init__(message, 409)


class PreconditionFailedException(BaseException):
    def __init__(self, message):
        super().__init__(message, 412)


class InternalServerErrorException(BaseException):
    def __init__(self, message):
        super().__init__(message, 500)
