"""
Initialization module for the Pydantic DTOs for account verification in the user
infrastructure layer.

This module imports and exposes the request and response DTOs used to validate and
serialize the requests and responses related to account verification. The __all__
attribute is used to explicitly define the names that will be exported when importing
this package.
"""

from .pydantic_verify_account_request_dto import PydanticVerifyAccountRequestDTO
from .pydantic_verify_account_response_dto import PydanticVerifyAccountResponseDTO

__all__ = [
    "PydanticVerifyAccountRequestDTO",
    "PydanticVerifyAccountResponseDTO",
]
