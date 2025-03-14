"""
Module that defines the response DTO for viewing an account in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the view account use case, containing the updated user model.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class PydanticViewAccountResponseDTO(BaseModel):
    """
    Response Data Transfer Object for viewing a user's account.

    Attributes:
        user (SQLModelUserModel): User model representing the user's account.
    """

    user: SQLModelUserModel
