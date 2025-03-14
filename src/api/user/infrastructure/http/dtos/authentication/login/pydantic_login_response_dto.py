"""
Module that defines the response DTO for login in the user infrastructure layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the login use case, containing the user model and the generated session token.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class PydanticLoginResponseDTO(BaseModel):
    """
    Response Data Transfer Object for user login.

    Attributes:
        user (SQLModelUserModel): User model representing the authenticated user.
        session_token (str): Session token generated after authentication.
    """

    user: SQLModelUserModel
    session_token: str
