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
from .persistence import (
    DragonflyValidationTokenRepository,
    SqlModelUserModel,
    SqlModelUserRepository,
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
    "SqlModelUserModel",
    "DragonflyValidationTokenRepository",
    "SqlModelUserRepository",
]
