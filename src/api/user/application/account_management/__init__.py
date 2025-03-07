"""
Initialization module for the account management functionality in the user application
layer.

This module imports and exposes all the use cases and DTOs related to managing the
user's account. The included functionalities are:
  - Account deletion (DeleteAccountDTO, DeleteAccountUseCase).
  - Account modification, which includes:
      - Password change (ChangePasswordDto, ChangePasswordUseCase).
      - Personal information modification (ChangePersonalInformationDTO,
        ChangePersonalInformationUseCase).
      - Password change request (RequestChangePasswordDto,
        RequestChangePasswordUseCase).
  - Account viewing (ViewAccountDTO, ViewAccountUseCase).

The __all__ attribute explicitly defines the names that will be exported when importing
this package.
"""

from .delete_account import DeleteAccountDTO, DeleteAccountUseCase
from .modify_user import (
    ChangePasswordDto,
    ChangePasswordUseCase,
    ChangePersonalInformationDTO,
    ChangePersonalInformationUseCase,
    RequestChangePasswordDto,
    RequestChangePasswordUseCase,
)
from .view_account import ViewAccountDTO, ViewAccountUseCase

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
]
