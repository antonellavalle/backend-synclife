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
    PydanticChangePasswordRequestDto,
    PydanticChangePasswordResponseDto,
    PydanticChangePersonalInformationRequestDto,
    PydanticChangePersonalInformationResponseDto,
    PydanticDeleteAccountRequestDto,
    PydanticDeleteAccountResponseDto,
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
    PydanticRequestChangePasswordRequestDto,
    PydanticRequestChangePasswordResponseDto,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
)

__all__ = [
    "FastApiAccountManagementController",
    "FastApiAuthenticationController",
    "PydanticChangePasswordRequestDto",
    "PydanticChangePasswordResponseDto",
    "PydanticChangePersonalInformationRequestDto",
    "PydanticChangePersonalInformationResponseDto",
    "PydanticDeleteAccountRequestDto",
    "PydanticDeleteAccountResponseDto",
    "PydanticRequestChangePasswordRequestDto",
    "PydanticRequestChangePasswordResponseDto",
    "PydanticViewAccountRequestDto",
    "PydanticViewAccountResponseDto",
    "PydanticLoginRequestDto",
    "PydanticLoginResponseDto",
    "PydanticRegisterRequestDto",
    "PydanticRegisterResponseDto",
    "PydanticVerifyAccountRequestDTO",
    "PydanticVerifyAccountResponseDTO",
]
