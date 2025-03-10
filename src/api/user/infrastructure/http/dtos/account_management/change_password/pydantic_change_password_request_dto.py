"""
Module that defines the request DTO for password change in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the password change request, and
provides a method to transform the request into the application layer DTO.
"""

from pydantic import BaseModel

from src.api.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDto,
)


class PydanticChangePasswordRequestDto(BaseModel):
    """
    Request Data Transfer Object for password change.

    Attributes:
        new_password (str): The new password to be set for the user.
    """

    new_password: str

    def to_application(self, validate_token: str) -> ChangePasswordDto:
        """
        Transforms the Pydantic DTO into an application layer DTO.

        Args:
            validate_token (str): Validation token that authorizes the password change.

        Returns:
            ChangePasswordDto: Application layer DTO with the necessary data to perform
                               the password change.
        """
        return ChangePasswordDto(
            validate_token=validate_token, new_password=self.new_password
        )
