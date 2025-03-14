"""
Module that defines the request DTO for viewing an account in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the account viewing request, and
provides a method to transform the infrastructure DTO into the corresponding application
layer DTO.
"""

from pydantic import BaseModel

from src.api.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDTO,
)


class PydanticViewAccountRequestDTO(BaseModel):
    """
    Request Data Transfer Object for viewing a user's account.

    This DTO is used to transform the HTTP request into the DTO object that the
    application layer expects to execute the view account use case.
    """

    def to_application(self, session_token: str) -> ViewAccountDTO:
        """
        Transforms the Pydantic DTO into the application layer DTO.

        Args:
            session_token (str): The user's session token, used to authorize the
                                 request.

        Returns:
            ViewAccountDTO: Application layer DTO with the session token included.
        """
        return ViewAccountDTO(session_token=session_token)
