"""
Initialization module for the Pydantic DTOs for the password change request in the user
infrastructure layer.

This module imports and exposes the request and response DTOs used to validate and
serialize the requests and responses related to the password change request. The __all__
attribute is used to explicitly define the names that will be exported when importing
this package.
"""

from .pydantic_request_change_password_request_dto import (
    PydanticRequestChangePasswordRequestDto,
)
from .pydantic_request_change_password_response_dto import (
    PydanticRequestChangePasswordResponseDto,
)

__all__ = [
    "PydanticRequestChangePasswordRequestDto",
    "PydanticRequestChangePasswordResponseDto",
]
