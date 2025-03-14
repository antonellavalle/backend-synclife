"""
Module that defines the response DTO for the password change request in the user
infrastructure layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the password change request use case, containing the updated user model.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class PydanticRequestChangePasswordResponseDTO(BaseModel):
    """
    Response Data Transfer Object for a user's password change request.

    Attributes:
        user (SQLModelUserModel): User model representing the updated user after the
                                  password change request.
    """

    user: SQLModelUserModel
