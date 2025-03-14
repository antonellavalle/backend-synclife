"""
Initialization module for the Pydantic DTOs for authentication in the user
infrastructure layer.

This module imports and exposes the request and response DTOs used to validate and
serialize the requests and responses related to authentication operations (login,
registration, and account verification). The __all__ attribute is used to explicitly
define the names that will be exported when importing this package.
"""

from .login import PydanticLoginRequestDTO, PydanticLoginResponseDTO
from .register import PydanticRegisterRequestDTO, PydanticRegisterResponseDTO
from .verify_account import (
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
)

__all__ = [
    "PydanticLoginRequestDTO",
    "PydanticLoginResponseDTO",
    "PydanticRegisterRequestDTO",
    "PydanticRegisterResponseDTO",
    "PydanticVerifyAccountRequestDTO",
    "PydanticVerifyAccountResponseDTO",
]
