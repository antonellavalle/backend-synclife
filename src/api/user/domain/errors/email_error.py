from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class EmailTypeError(Enum):
    INVALID_EMAIL = {"msg": "The email address is not valid.", "code": 400}


class EmailError(UserError):
    def __init__(self, error_type: EmailTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
