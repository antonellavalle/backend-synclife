"""
Module that defines the request DTO for login in the user infrastructure layer.

This DTO uses Pydantic to validate and serialize the login request, and provides a
method to transform the infrastructure DTO into the corresponding application layer DTO.
"""

from pydantic import BaseModel, EmailStr

from src.api.user.application.authentication.login.login_dto import LoginDTO


class PydanticLoginRequestDTO(BaseModel):
    """
    Request Data Transfer Object for user login.

    Attributes:
        email (EmailStr): The user's email address.
        password (str): The user's password.
    """

    email: EmailStr
    password: str

    def to_application(self) -> LoginDTO:
        """
        Transforms the Pydantic DTO into the application layer DTO.

        Returns:
            LoginDTO: Application layer DTO with the data required to log in.
        """
        return LoginDTO(email=self.email, password=self.password)
