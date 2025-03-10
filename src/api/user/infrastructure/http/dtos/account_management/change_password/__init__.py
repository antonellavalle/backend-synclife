"""
Initialization module for the Pydantic DTOs for password change in the user
infrastructure layer.

This module imports and exposes the request and response DTOs that are used to validate
and serialize the requests and responses related to password change. The __all__
attribute is used to explicitly define the names that will be exported when importing
this package.
"""

from .pydantic_change_password_request_dto import PydanticChangePasswordRequestDto
from .pydantic_change_password_response_dto import PydanticChangePasswordResponseDto

__all__ = ["PydanticChangePasswordRequestDto", "PydanticChangePasswordResponseDto"]
