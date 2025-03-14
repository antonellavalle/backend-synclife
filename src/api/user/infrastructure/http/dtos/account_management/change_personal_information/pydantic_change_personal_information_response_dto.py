"""
Module that defines the response DTO for modifying personal information in the user
infrastructure layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the use case for modifying personal information, containing the updated user model.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticChangePersonalInformationResponseDTO(BaseModel):
    """
    Response Data Transfer Object for modifying the user's personal information.

    Attributes:
        user (SqlModelUserModel): User model representing the updated user after the
                                  modification.
    """

    user: SqlModelUserModel
