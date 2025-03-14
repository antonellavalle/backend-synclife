"""
Module that defines the request DTO for account deletion in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the account deletion request, and
provides a method to transform the infrastructure DTO into the corresponding application
layer DTO.
"""

from pydantic import BaseModel

from src.api.user.application.account_management.delete_account.delete_account_dto import (  # noqa: E501
    DeleteAccountDTO,
)


class PydanticDeleteAccountRequestDTO(BaseModel):
    """
    Request Data Transfer Object for user account deletion.

    This DTO is used to transform the HTTP account deletion request into the object that
    will be interpreted by the application layer.
    """

    def to_application(self, session_token: str) -> DeleteAccountDTO:
        """
        Transforms the Pydantic DTO into the application layer DTO.

        Args:
            session_token (str): Session token that authorizes the account deletion
                                 request.

        Returns:
            DeleteAccountDTO: Application layer DTO with the session token.
        """
        return DeleteAccountDTO(session_token=session_token)
