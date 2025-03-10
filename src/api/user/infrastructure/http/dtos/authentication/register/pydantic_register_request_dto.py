"""
Module that defines the request DTO for user registration in the user infrastructure
layer.

This DTO uses Pydantic to validate and serialize the user registration request, and
provides a method to transform the infrastructure DTO into the corresponding application
layer DTO.
"""

from datetime import date

from pydantic import BaseModel, EmailStr

from src.api.user.application.authentication.register.register_dto import RegisterDTO


class PydanticRegisterRequestDto(BaseModel):
    """
    Request Data Transfer Object for user registration.

    Attributes:
        email (EmailStr): The user's email address.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        phone (str): The user's phone number.
        password (str): The user's password.
        birth_date (date): The user's date of birth.
    """

    email: EmailStr
    first_name: str
    last_name: str
    phone: str
    password: str
    birth_date: date

    def to_application(self, url: str) -> RegisterDTO:
        """
        Transforms the Pydantic DTO into the application layer DTO.

        Args:
            url (str): Base URL to be used for account verification or the registration
                       process.

        Returns:
            RegisterDTO: Application layer DTO with the necessary data to register the
                         user.
        """
        return RegisterDTO(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            phone=self.phone,
            password=self.password,
            birth_date=self.birth_date,
            url=url,
        )
