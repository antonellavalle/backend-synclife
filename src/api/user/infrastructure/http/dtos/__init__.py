"""
Initialization module for the user infrastructure DTOs.

This module imports and exposes all the DTOs from the infrastructure layer related to
account management and authentication functionalities.
It includes the request and response DTOs for:
  - Password Change.
  - Personal Information Modification.
  - Account Deletion.
  - Password Change Request.
  - Account Viewing.
  - Login.
  - Registration.
  - Account Verification.

The __all__ attribute explicitly defines the names that will be exported when importing
this package.
"""

from .account_management import (
    PydanticChangePasswordRequestDto,
    PydanticChangePasswordResponseDto,
    PydanticChangePersonalInformationRequestDto,
    PydanticChangePersonalInformationResponseDto,
    PydanticDeleteAccountRequestDto,
    PydanticDeleteAccountResponseDto,
    PydanticRequestChangePasswordRequestDto,
    PydanticRequestChangePasswordResponseDto,
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
)
from .authentication import (
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
)

__all__ = [
    "PydanticLoginRequestDto",
    "PydanticLoginResponseDto",
    "PydanticRegisterRequestDto",
    "PydanticRegisterResponseDto",
    "PydanticViewAccountRequestDto",
    "PydanticViewAccountResponseDto",
    "PydanticDeleteAccountRequestDto",
    "PydanticDeleteAccountResponseDto",
    "PydanticChangePasswordRequestDto",
    "PydanticChangePasswordResponseDto",
    "PydanticChangePersonalInformationRequestDto",
    "PydanticChangePersonalInformationResponseDto",
    "PydanticVerifyAccountRequestDTO",
    "PydanticVerifyAccountResponseDTO",
    "PydanticRequestChangePasswordRequestDto",
    "PydanticRequestChangePasswordResponseDto",
]
