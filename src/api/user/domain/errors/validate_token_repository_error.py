from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class ValidateTokenRepositoryTypeError(Enum):
    INVALID_TOKEN = {"msg": "Verification token is invalid.", "code": 400}
    ALREADY_VERIFIED = {"msg": "The account is already verified.", "code": 400}


class ValidateTokenRepositoryError(UserError):
    def __init__(self, error_type: ValidateTokenRepositoryTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
