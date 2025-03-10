"""
Module that defines the request DTO for requesting a password change in the user
infrastructure layer.

This DTO uses Pydantic to validate and serialize the password change request, and
provides a method to convert the infrastructure DTO into the corresponding application
layer DTO.
"""

from pydantic import BaseModel, EmailStr

from src.api.user.application.account_management.modify_user.request_change_password.request_change_password_dto import (  # noqa: E501
    RequestChangePasswordDto,
)


class PydanticRequestChangePasswordRequestDto(BaseModel):
    """
    Request Data Transfer Object for requesting a user's password change.

    Attributes:
        email (EmailStr): The user's email address.
    """

    email: EmailStr

    def to_application(self, url: str) -> RequestChangePasswordDto:
        """
        Transforms the Pydantic DTO into the application layer DTO.

        Args:
            url (str): Base URL to be used for generating the password change link.

        Returns:
            RequestChangePasswordDto: Application layer DTO with the necessary data to
                                      request a password change.
        """
        return RequestChangePasswordDto(email=self.email, url=url)
