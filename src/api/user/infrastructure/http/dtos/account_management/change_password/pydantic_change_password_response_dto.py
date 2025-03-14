"""
Module that defines the response DTO for password change in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the password change use case, containing the updated user information.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class PydanticChangePasswordResponseDTO(BaseModel):
    """
    Response Data Transfer Object for password change.

    Attributes:
        user (SQLModelUserModel): User model representing the updated user after the
                                  password change.
    """

    user: SQLModelUserModel
