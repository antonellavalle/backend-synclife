"""
Initialization module for the password change functionality in the user application.

This module imports and exposes the components required for the password change process,
including the DTO (ChangePasswordDTO) and the use case (ChangePasswordUseCase). The
__all__ attribute is used to explicitly define the names that will be exported when this
package is imported.
"""

from .change_password_dto import ChangePasswordDTO
from .change_password_use_case import ChangePasswordUseCase

__all__ = ["ChangePasswordDTO", "ChangePasswordUseCase"]
