"""
User infrastructure initialization module.

This module centralizes the import and exposure of all components from the user
infrastructure layer, including:
  - The HTTP layer: Controllers and Pydantic DTOs for account management and
                    authentication.
  - The persistence layer: Repositories and persistence models, such as
                           DragonflyValidationTokenRepository, SqlModelUserModel, and
                           SqlModelUserRepository.

The __all__ attribute is used to explicitly define the names that will be exported when
importing this package.
"""

from .http import (
    FastApiAccountManagementController,
    FastApiAuthenticationController,
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
from .persistence import (
    DragonflyValidationTokenRepository,
    SqlModelUserModel,
    SqlModelUserRepository,
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
    "SqlModelUserModel",
    "DragonflyValidationTokenRepository",
    "SqlModelUserRepository",
]
