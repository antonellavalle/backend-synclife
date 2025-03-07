"""
Initialization module for the account verification functionality in the user
application.

This module imports and exposes the components necessary for the account verification
process, including the DTO (VerifyAccountDTO) and the use case (VerifyAccountUseCase).
The __all__ attribute is used to explicitly define the names that will be exported when
importing this package.
"""

from .verify_account_dto import VerifyAccountDTO
from .verify_account_use_case import VerifyAccountUseCase

__all__ = ["VerifyAccountDTO", "VerifyAccountUseCase"]
