"""
Module that defines the response DTO for account deletion in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the account deletion use case, containing the updated user model.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticDeleteAccountResponseDTO(BaseModel):
    """
    Response Data Transfer Object for account deletion.

    Attributes:
        user (SqlModelUserModel): User model representing the deleted or
                                  marked-as-deleted user.
    """

    user: SqlModelUserModel
