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
    PydanticChangePasswordRequestDTO,
    PydanticChangePasswordResponseDTO,
    PydanticChangePersonalInformationRequestDTO,
    PydanticChangePersonalInformationResponseDTO,
    PydanticDeleteAccountRequestDTO,
    PydanticDeleteAccountResponseDTO,
    PydanticRequestChangePasswordRequestDTO,
    PydanticRequestChangePasswordResponseDTO,
    PydanticViewAccountRequestDTO,
    PydanticViewAccountResponseDTO,
)
from .authentication import (
    PydanticLoginRequestDTO,
    PydanticLoginResponseDTO,
    PydanticRegisterRequestDTO,
    PydanticRegisterResponseDTO,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
)

__all__ = [
    "PydanticLoginRequestDTO",
    "PydanticLoginResponseDTO",
    "PydanticRegisterRequestDTO",
    "PydanticRegisterResponseDTO",
    "PydanticViewAccountRequestDTO",
    "PydanticViewAccountResponseDTO",
    "PydanticDeleteAccountRequestDTO",
    "PydanticDeleteAccountResponseDTO",
    "PydanticChangePasswordRequestDTO",
    "PydanticChangePasswordResponseDTO",
    "PydanticChangePersonalInformationRequestDTO",
    "PydanticChangePersonalInformationResponseDTO",
    "PydanticVerifyAccountRequestDTO",
    "PydanticVerifyAccountResponseDTO",
    "PydanticRequestChangePasswordRequestDTO",
    "PydanticRequestChangePasswordResponseDTO",
]
