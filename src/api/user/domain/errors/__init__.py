"""
Initialization module for user domain errors.

This module imports and exposes the various errors related to user data validation and
handling, including errors for email, full name, password, phone, repository,
validation, and token verification. The __all__ attribute is used to explicitly define
the names that will be exported when importing this package.
"""

from .email_error import EmailError, EmailTypeError
from .full_name_error import FullNameError, FullNameTypeError
from .password_error import PasswordError, PasswordTypeError
from .phone_error import PhoneError, PhoneTypeError
from .user_repository_error import UserRepositoryError, UserRepositoryTypeError
from .user_validation_error import UserValidationError, UserValidationTypeError
from .validate_token_repository_error import (
    ValidateTokenRepositoryError,
    ValidateTokenRepositoryTypeError,
)

__all__ = [
    "EmailError",
    "EmailTypeError",
    "FullNameError",
    "FullNameTypeError",
    "PasswordError",
    "PasswordTypeError",
    "UserValidationError",
    "UserValidationTypeError",
    "PhoneError",
    "PhoneTypeError",
    "UserRepositoryError",
    "UserRepositoryTypeError",
    "ValidateTokenRepositoryError",
    "ValidateTokenRepositoryTypeError",
]
