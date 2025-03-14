"""
Initialization module for the Pydantic DTOs for modifying personal information
in the user infrastructure layer.

This module imports and exposes the request and response DTOs used to validate and
serialize the requests and responses related to the modification of the user's personal
information. The __all__ attribute is used to explicitly define the names that will be
exported when importing this package.
"""

from .pydantic_change_personal_information_request_dto import (
    PydanticChangePersonalInformationRequestDTO,
)
from .pydantic_change_personal_information_response_dto import (
    PydanticChangePersonalInformationResponseDTO,
)

__all__ = [
    "PydanticChangePersonalInformationRequestDTO",
    "PydanticChangePersonalInformationResponseDTO",
]
