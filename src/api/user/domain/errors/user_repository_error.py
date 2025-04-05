from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class UserRepositoryTypeError(Enum):
    ALREADY_EXISTS = {"msg": "A user with this email already exists.", "code": 400}
    NOT_FOUND = {"msg": "The user is not registered.", "code": 400}
    OPERATION_FAILED = {"msg": "The operation failed.", "code": 400}
    NOT_VERIFIED = {"msg": "The user is not verified.", "code": 400}


class UserRepositoryError(UserError):
    def __init__(self, error_type: UserRepositoryTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
