"""
Module that defines the use case for user registration in the application.

This module contains the RegisterUseCase class, which implements the logic to register
a user. The registration process includes:
  - Checking if the email is already registered.
  - Sending a verification email if the account is not verified.
  - Creating a new User entity and persisting it in the repository.
  - Sending a validation email to complete the registration process.

It uses three repositories:
  - UserRepository: For user management.
  - SMTPEmailSenderRepository: For sending emails.
  - ValidationTokenRepository: For creating and managing validation tokens.
"""

from datetime import datetime

from src.api.shared.domain.repositories import SMTPEmailSenderRepository
from src.api.shared.domain.value_objects import Uuid
from src.api.user.application.authentication.register.register_dto import RegisterDTO
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors import UserRepositoryError, UserRepositoryTypeError
from src.api.user.domain.repositories import UserRepository, ValidationTokenRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects import Email, FullName, Password, Phone


class RegisterUseCase:
    """
    Use case for user registration.

    This class implements the logic needed to register a user in the system. The process
    includes:
      1. Checking if the email is already registered.
      2. Sending a validation email if the user already exists but has not been
         verified.
      3. Creating a new User entity and persisting it in the repository.
      4. Generating a validation token and sending an email to complete the
         registration.

    Attributes:
        __user_repository (UserRepository): Repository for user management.
        __smtp_email_sender_repository (SMTPEmailSenderRepository): Repository for
                                                                    sending emails.
        __validate_user_repository (ValidationTokenRepository): Repository for managing
                                                                validation tokens.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        smtp_email_sender_repository: SMTPEmailSenderRepository,
        validate_user_repository: ValidationTokenRepository,
    ) -> None:
        """
        Initializes a new instance of RegisterUseCase.

        Args:
            user_repository (UserRepository): User repository.
            smtp_email_sender_repository (SMTPEmailSenderRepository): Repository for
                                                                      sending emails.
            validate_user_repository (ValidationTokenRepository): Repository for
                                                                  creating and managing
                                                                  validation tokens.
        """
        self.__user_repository = user_repository
        self.__smtp_email_sender_repository = smtp_email_sender_repository
        self.__validate_user_repository = validate_user_repository

    def __send_email(self, to: str, url: str) -> None:
        """
        Sends a validation email.

        Uses the email sending repository to send a verification message to the user,
        including the generated link for account validation.

        Args:
            to (str): Email address of the recipient.
            url (str): URL containing the validation token to complete the registration.
        """
        self.__smtp_email_sender_repository.send_email(
            to=to,
            subject="Validate account",
            body="Click on the following link to validate your account and finish the"
            " registration process.\n\n" + url,
        )

    def execute(self, dto: RegisterDTO) -> User:
        """
        Executes the user registration use case.

        Performs the following operations:
          1. Converts the email from the DTO into an Email object.
          2. Checks if a user is already registered with that email.
          3. If the user exists and the account is already verified, raises an
             exception. If the user exists but is not verified, generates a validation
             token, sends an email, and returns the existing user.
          4. If the email is not registered, verifies that it does not already exist and
             creates a new User entity.
          5. Generates a validation token, sends a validation email, and saves the user
             in the repository.
          6. Returns the created or updated User object.

        Args:
            dto (RegisterDTO): Object containing the data needed to register the user,
                               including email, password, first name, last name, birth
                               date, phone, and the base URL for validation.

        Returns:
            User: The registered or updated User object.

        Raises:
            UserRepositoryError: If the user already exists and the account is verified,
                                 or if an error occurs during the operation.
        """
        email = Email(dto.email)

        existing_user = self.__user_repository.find_by_email(email, True)
        if existing_user is not None:
            if existing_user.account_verified:
                raise UserRepositoryError(UserRepositoryTypeError.USER_ALREADY_EXISTS)
            else:
                verify_token = (
                    self.__validate_user_repository.create_validation_request(
                        user_uuid=existing_user.uuid
                    )
                )
                self.__send_email(to=str(email), url=f"{dto.url}/{verify_token}")
                return existing_user

        UserRepositoryValidator.is_email_already_registered(
            self.__user_repository, email
        )

        user = User(
            uuid=Uuid(),
            email=email,
            password=Password(dto.password),
            full_name=FullName(dto.first_name, dto.last_name),
            birth_date=dto.birth_date,
            phone=Phone(dto.phone),
            account_verified=False,
            is_deleted=False,
            created_at=datetime.now(),
            updated_at=None,
        )

        verify_token = self.__validate_user_repository.create_validation_request(
            user_uuid=user.uuid
        )
        self.__send_email(to=str(email), url=f"{dto.url}/{verify_token}")
        self.__user_repository.save(user=user)

        return user
