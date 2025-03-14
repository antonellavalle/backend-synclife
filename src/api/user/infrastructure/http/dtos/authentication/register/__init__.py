"""
Initialization module for the Pydantic DTOs for registration in the user infrastructure
layer.

This module imports and exposes the request and response DTOs used to validate and
serialize the requests and responses related to user registration. The __all__ attribute
is used to explicitly define the names that will be exported when importing this
package.
"""

from .pydantic_register_request_dto import PydanticRegisterRequestDTO
from .pydantic_register_response_dto import PydanticRegisterResponseDTO

__all__ = ["PydanticRegisterRequestDTO", "PydanticRegisterResponseDTO"]
