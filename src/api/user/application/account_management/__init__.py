"""
Initialization module for the account management functionality in the user application
layer.

This module imports and exposes all the use cases and DTOs related to managing the
user's account. The included functionalities are:
  - Account deletion (DeleteAccountDTO, DeleteAccountUseCase).
  - Account modification, which includes:
      - Password change (ChangePasswordDTO, ChangePasswordUseCase).
      - Personal information modification (ChangePersonalInformationDTO,
        ChangePersonalInformationUseCase).
      - Password change request (RequestChangePasswordDTO,
        RequestChangePasswordUseCase).
  - Account viewing (ViewAccountDTO, ViewAccountUseCase).

The __all__ attribute explicitly defines the names that will be exported when importing
this package.
"""

from .delete_account import DeleteAccountDTO, DeleteAccountUseCase
from .modify_user import (
    ChangePasswordDTO,
    ChangePasswordUseCase,
    ChangePersonalInformationDTO,
    ChangePersonalInformationUseCase,
    RequestChangePasswordDTO,
    RequestChangePasswordUseCase,
)
from .view_account import ViewAccountDTO, ViewAccountUseCase

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
]
