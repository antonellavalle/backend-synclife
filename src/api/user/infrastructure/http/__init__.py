"""
Initialization module for the HTTP layer of the user infrastructure.

This module imports and exposes all the components of the HTTP layer, which include:
  - Controllers: FastApiAccountManagementController and FastApiAuthenticationController.
  - Pydantic DTOs: Used for validating and serializing the requests and responses in
                   account management and authentication operations.

The __all__ attribute is used to explicitly define the names that will be exported when
importing this package.
"""

from .controllers import (
    FastApiAccountManagementController,
    FastApiAuthenticationController,
)
from .dtos import (
    PydanticChangePasswordRequestDTO,
    PydanticChangePasswordResponseDTO,
    PydanticChangePersonalInformationRequestDTO,
    PydanticChangePersonalInformationResponseDTO,
    PydanticDeleteAccountRequestDTO,
    PydanticDeleteAccountResponseDTO,
    PydanticLoginRequestDTO,
    PydanticLoginResponseDTO,
    PydanticRegisterRequestDTO,
    PydanticRegisterResponseDTO,
    PydanticRequestChangePasswordRequestDTO,
    PydanticRequestChangePasswordResponseDTO,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
    PydanticViewAccountRequestDTO,
    PydanticViewAccountResponseDTO,
)

__all__ = [
    "FastApiAccountManagementController",
    "FastApiAuthenticationController",
    "PydanticChangePasswordRequestDTO",
    "PydanticChangePasswordResponseDTO",
    "PydanticChangePersonalInformationRequestDTO",
    "PydanticChangePersonalInformationResponseDTO",
    "PydanticDeleteAccountRequestDTO",
    "PydanticDeleteAccountResponseDTO",
    "PydanticRequestChangePasswordRequestDTO",
    "PydanticRequestChangePasswordResponseDTO",
    "PydanticViewAccountRequestDTO",
    "PydanticViewAccountResponseDTO",
    "PydanticLoginRequestDTO",
    "PydanticLoginResponseDTO",
    "PydanticRegisterRequestDTO",
    "PydanticRegisterResponseDTO",
    "PydanticVerifyAccountRequestDTO",
    "PydanticVerifyAccountResponseDTO",
]
