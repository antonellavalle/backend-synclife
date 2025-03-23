from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class PhoneTypeError(Enum):
    INVALID_PHONE = {"msg": "The phone number is not valid.", "code": 400}


class PhoneError(UserError):
    def __init__(self, error_type: PhoneTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
