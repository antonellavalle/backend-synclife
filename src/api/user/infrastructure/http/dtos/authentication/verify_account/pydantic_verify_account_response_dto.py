"""
Module that defines the response DTO for account verification in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the account verification use case, containing the updated user model and the generated
session token.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticVerifyAccountResponseDTO(BaseModel):
    """
    Response Data Transfer Object for user account verification.

    Attributes:
        user (SqlModelUserModel): User model representing the verified user.
        session_token (str): Session token generated after account verification.
    """

    user: SqlModelUserModel
    session_token: str
