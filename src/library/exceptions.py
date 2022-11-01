class BadRequestException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UnauthorizedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ForbiddenException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class MethodNotAllowedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ConflictException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PreconditionFailedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InternalServerErrorException(Exception):
    def __init__(self, message):
        super().__init__(message)
