from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class PasswordTypeError(Enum):
    TOO_SHORT = {"msg": "The password must be at least 8 characters long.", "code": 400}
    MISSING_NUMBER = {
        "msg": "The password must contain at least one number.",
        "code": 400,
    }
    MISSING_UPPERCASE = {
        "msg": "The password must contain at least one uppercase letter.",
        "code": 400,
    }
    MISSING_LOWERCASE = {
        "msg": "The password must contain at least one lowercase letter.",
        "code": 400,
    }
    MISSING_SPECIAL = {
        "msg": "The password must contain at least one special character.",
        "code": 400,
    }
    WEAK_PASSWORD = {"msg": "The password is too weak.", "code": 400}


class PasswordError(UserError):
    def __init__(self, error_type: PasswordTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
