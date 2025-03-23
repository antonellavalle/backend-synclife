from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class UserValidationTypeError(Enum):
    INVALID_BIRTHDATE = {"msg": "The birthdate is not valid.", "code": 400}
    INVALID_CREDENTIALS = {
        "msg": "The email or password is incorrect.",
        "code": 400,
    }


class UserValidationError(UserError):
    def __init__(self, error_type: UserValidationTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
