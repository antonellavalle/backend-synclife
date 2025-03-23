from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class FullNameTypeError(Enum):
    INVALID_NAME = {"msg": "The first name or last name is not valid.", "code": 400}
    INVALID_NAME_FORMAT = {
        "msg": "The first name or last name contains invalid characters.",
        "code": 400,
    }
    NAME_TOO_LONG = {"msg": "The first name or last name is too long.", "code": 400}


class FullNameError(UserError):
    def __init__(self, error_type: FullNameTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
