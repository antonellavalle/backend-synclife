"""
Module that defines the request DTO for modifying personal information in the user
infrastructure layer.

This DTO uses Pydantic to validate and serialize the personal information modification
request. Additionally, it provides a method to transform the Pydantic DTO into the
application layer DTO.
"""

from datetime import date

from pydantic import BaseModel, EmailStr

from src.api.user.application.account_management.modify_user.change_personal_information.change_personal_information_dto import (  # noqa: E501
    ChangePersonalInformationDTO,
)


class PydanticChangePersonalInformationRequestDTO(BaseModel):
    """
    Data Transfer Object for requesting the modification of a user's personal
    information.

    Attributes:
        email (EmailStr): The user's email address.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        birth_date (date): The user's date of birth.
        phone (str): The user's phone number.
    """

    email: EmailStr
    first_name: str
    last_name: str
    birth_date: date
    phone: str

    def to_application(self, session_token: str) -> ChangePersonalInformationDTO:
        """
        Transforms the Pydantic DTO into the application layer DTO.

        Args:
            session_token (str): The user's session token used to validate the request.

        Returns:
            ChangePersonalInformationDTO: Application layer DTO with the necessary data
                                          to modify the personal information.
        """
        return ChangePersonalInformationDTO(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            birth_date=self.birth_date,
            phone=self.phone,
            session_token=session_token,
        )
