"""
Module that defines the request DTO for account verification in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the account verification request, and
provides a method to transform the infrastructure DTO into the corresponding application
layer DTO.
"""

from pydantic import BaseModel

from src.api.user.application.authentication.verify_account.verify_account_dto import (
    VerifyAccountDTO,
)


class PydanticVerifyAccountRequestDTO(BaseModel):
    """
    Request Data Transfer Object for user account verification.

    This DTO is used to transform the HTTP request into the DTO object expected by the
    application layer to execute the account verification use case.
    """

    def to_application(self, validate_token: str) -> VerifyAccountDTO:
        """
        Transforms the Pydantic DTO into the application layer DTO.

        Args:
            validate_token (str): Validation token used to authorize account
                                  verification.

        Returns:
            VerifyAccountDTO: Application layer DTO with the validation token
                              incorporated.
        """
        return VerifyAccountDTO(validate_token=validate_token)
