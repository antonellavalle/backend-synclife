"""
Module that defines the response DTO for login in the user infrastructure layer.

This DTO uses Pydantic to validate and serialize the response returned after executing
the login use case, containing the user model and the generated session token.
"""

from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticLoginResponseDto(BaseModel):
    """
    Response Data Transfer Object for user login.

    Attributes:
        user (SqlModelUserModel): User model representing the authenticated user.
        session_token (str): Session token generated after authentication.
    """

    user: SqlModelUserModel
    session_token: str
