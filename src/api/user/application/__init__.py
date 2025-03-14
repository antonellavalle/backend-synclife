"""
Initialization module for the user application layer.

This module imports and exposes all the use cases and DTOs related to the
functionalities of account management and authentication in the user application. The
following components are included:

  Account Management:
    - Account deletion: DeleteAccountDTO, DeleteAccountUseCase
    - Password change: ChangePasswordDTO, ChangePasswordUseCase
    - Personal information modification: ChangePersonalInformationDTO,
                                         ChangePersonalInformationUseCase
    - Password change request: RequestChangePasswordDTO, RequestChangePasswordUseCase
    - Account viewing: ViewAccountDTO, ViewAccountUseCase

  Authentication:
    - Login: LoginDTO, LoginUseCase
    - Registration: RegisterDTO, RegisterUseCase
    - Account verification: VerifyAccountDTO, VerifyAccountUseCase

The __all__ attribute explicitly defines the names that will be exported when importing
this package.
"""

from .account_management import (
    ChangePasswordDTO,
    ChangePasswordUseCase,
    ChangePersonalInformationDTO,
    ChangePersonalInformationUseCase,
    DeleteAccountDTO,
    DeleteAccountUseCase,
    RequestChangePasswordDTO,
    RequestChangePasswordUseCase,
    ViewAccountDTO,
    ViewAccountUseCase,
)
from .authentication import (
    LoginDTO,
    LoginUseCase,
    RegisterDTO,
    RegisterUseCase,
    VerifyAccountDTO,
    VerifyAccountUseCase,
)

__all__ = [
    "DeleteAccountDTO",
    "DeleteAccountUseCase",
    "ChangePasswordDTO",
    "ChangePasswordUseCase",
    "ChangePersonalInformationDTO",
    "ChangePersonalInformationUseCase",
    "RequestChangePasswordDTO",
    "RequestChangePasswordUseCase",
    "ViewAccountDTO",
    "ViewAccountUseCase",
    "LoginDTO",
    "LoginUseCase",
    "RegisterDTO",
    "RegisterUseCase",
    "VerifyAccountDTO",
    "VerifyAccountUseCase",
]
