"""
Initialization module for the user package.

This module centralizes the import and exposure of all components belonging to the
domain, application, and infrastructure layers of the user module. It includes:

  - In the application layer: DTOs and use cases for operations such as registration,
                              login, account verification, account deletion, password
                              change, personal information modification, and password
                              change request.
  - In the domain layer: Entities, value objects, and errors (along with their
                         enumerations) associated with the validation, management, and
                         persistence of users, as well as the repository interface and
                         its validators.
  - In the infrastructure layer: Concrete implementations of the HTTP controllers (using
                                 FastAPI), Pydantic DTOs for validation and
                                 serialization, and the persistence models and
                                 repositories (SQLModel, Dragonfly, etc.).

The __all__ attribute explicitly defines the names that will be exported when importing
this package.
"""

from .application import (
    ChangePasswordDto,
    ChangePasswordUseCase,
    ChangePersonalInformationDTO,
    ChangePersonalInformationUseCase,
    DeleteAccountDTO,
    DeleteAccountUseCase,
    LoginDTO,
    LoginUseCase,
    RegisterDTO,
    RegisterUseCase,
    RequestChangePasswordDto,
    RequestChangePasswordUseCase,
    VerifyAccountDTO,
    VerifyAccountUseCase,
    ViewAccountDTO,
    ViewAccountUseCase,
)
from .domain import (
    Email,
    EmailError,
    EmailTypeError,
    FullName,
    FullNameError,
    FullNameTypeError,
    Password,
    PasswordError,
    PasswordTypeError,
    Phone,
    PhoneError,
    PhoneTypeError,
    User,
    UserRepository,
    UserRepositoryError,
    UserRepositoryTypeError,
    UserRepositoryValidator,
    UserValidationError,
    UserValidationTypeError,
    ValidateTokenRepositoryError,
    ValidateTokenRepositoryTypeError,
    ValidationTokenRepository,
)
from .infrastructure import (
    DragonflyValidationTokenRepository,
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
    SqlModelUserModel,
    SqlModelUserRepository,
)

__all__ = [
    "DeleteAccountDTO",
    "DeleteAccountUseCase",
    "ChangePasswordDto",
    "ChangePasswordUseCase",
    "ChangePersonalInformationDTO",
    "ChangePersonalInformationUseCase",
    "RequestChangePasswordDto",
    "RequestChangePasswordUseCase",
    "ViewAccountDTO",
    "ViewAccountUseCase",
    "LoginDTO",
    "LoginUseCase",
    "RegisterDTO",
    "RegisterUseCase",
    "VerifyAccountDTO",
    "VerifyAccountUseCase",
    "User",
    "EmailError",
    "EmailTypeError",
    "FullNameError",
    "FullNameTypeError",
    "PasswordError",
    "PasswordTypeError",
    "UserValidationError",
    "UserValidationTypeError",
    "PhoneError",
    "PhoneTypeError",
    "UserRepositoryError",
    "UserRepositoryTypeError",
    "UserRepository",
    "ValidationTokenRepository",
    "UserRepositoryValidator",
    "Email",
    "FullName",
    "Password",
    "Phone",
    "ValidateTokenRepositoryError",
    "ValidateTokenRepositoryTypeError",
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
