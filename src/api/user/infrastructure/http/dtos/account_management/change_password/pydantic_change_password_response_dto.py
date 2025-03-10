"""
Module that defines the response DTO for password change in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the password change use case, containing the updated user information.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticChangePasswordResponseDto(BaseModel):
    """
    Response Data Transfer Object for password change.

    Attributes:
        user (SqlModelUserModel): User model representing the updated user after the
                                  password change.
    """

    user: SqlModelUserModel
