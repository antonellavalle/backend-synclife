"""
Module that defines the response DTO for user registration in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the registration use case, containing the created or updated user model.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticRegisterResponseDto(BaseModel):
    """
    Response Data Transfer Object for user registration.

    Attributes:
        user (SqlModelUserModel): User model representing the registered user.
    """

    user: SqlModelUserModel
