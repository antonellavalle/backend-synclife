"""
Module that defines errors related to token validation in the user domain repository.

This module contains:
  - ValidateTokenRepositoryTypeError: Enumeration that specifies the types of errors
                                      related to token validation, including invalid
                                      tokens and already verified accounts.
  - ValidateTokenRepositoryError: Exception raised when an error occurs during token
                                  validation in the repository.
"""

from enum import Enum
from typing import Dict, cast

from src.api.user.domain.errors.user_error import UserError


class ValidateTokenRepositoryTypeError(Enum):
    """
    Enumeration of error types for token validation in the repository.

    Each member of this enumeration contains a dictionary with a descriptive message and
    an error code, which is used to identify specific errors during token validation.

    Attributes:
        INVALID_TOKEN (Dict[str, int | str]): Error indicating that the verification
                                              token is invalid.
        ALREADY_VERIFIED (Dict[str, int | str]): Error indicating that the account is
                                                 already verified.
    """

    INVALID_TOKEN = {"msg": "Verification token is invalid.", "code": 400}
    ALREADY_VERIFIED = {"msg": "The account is already verified.", "code": 400}


class ValidateTokenRepositoryError(UserError):
    """
    Exception raised when an error occurs during token validation in the repository.

    This exception inherits from UserError and is initialized using a value from
    ValidateTokenRepositoryTypeError, thereby setting the corresponding descriptive
    message and error code.

    Args:
        error_type (ValidateTokenRepositoryTypeError): Specific error type related to
                                                       token validation.
    """

    def __init__(self, error_type: ValidateTokenRepositoryTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
