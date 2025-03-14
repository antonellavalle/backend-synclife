"""
Module that defines the use case for requesting a password change in the user
application.

This module contains the RequestChangePasswordUseCase class, which implements the logic
to initiate the password change process.The process includes:
  1. Finding the user by the provided email.
  2. Generating a validation token associated with the user.
  3. Sending an email with a link that contains the token so that the user can change
     their password.
  4. Returning the corresponding User object.
"""

from src.api.shared.domain.repositories.smtp_email_sender_repository import (
    SMTPEmailSenderRepository,
)
from src.api.user.application.account_management.modify_user.request_change_password import (  # noqa: E501
    RequestChangePasswordDTO,
)
from src.api.user.domain.entities.user import User
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.repositories.validation_token_repository import (
    ValidationTokenRepository,
)
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects.email import Email


class RequestChangePasswordUseCase:
    """
    Use case for requesting a user's password change.

    This class implements the logic required to initiate the password change process.
    The process consists of:
      1. Finding the user based on the provided email.
      2. Generating a validation token for the user.
      3. Sending an email to the user with a link that contains the validation token so
         they can change their password.
      4. Returning the corresponding User object.

    Attributes:
        __user_repository (UserRepository): Repository for managing users.
        __smtp_email_sender_repository (SMTPEmailSenderRepository): Repository for
                                                                    sending emails.
        __validation_token_repository (ValidationTokenRepository): Repository for
                                                                   creating and managing
                                                                   validation tokens.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        smtp_email_sender_repository: SMTPEmailSenderRepository,
        validation_token_repository: ValidationTokenRepository,
    ) -> None:
        """
        Initializes a new instance of RequestChangePasswordUseCase.

        Args:
            user_repository (UserRepository): User repository.
            smtp_email_sender_repository (SMTPEmailSenderRepository): Repository for
                                                                      sending emails.
            validation_token_repository (ValidationTokenRepository): Repository for
                                                                     creating and
                                                                     managing validation
                                                                     tokens.
        """
        self.__user_repository = user_repository
        self.__smtp_email_sender_repository = smtp_email_sender_repository
        self.__validation_token_repository = validation_token_repository

    def __send_email(self, to: str, url: str) -> None:
        """
        Sends an email with the link to change the password.

        Uses the email sending repository to send a message to the user, which includes
        a link generated from the validation token.

        Args:
            to (str): The recipient's email address.
            url (str): URL that contains the validation token to complete the password
                       change.
        """
        self.__smtp_email_sender_repository.send_email(
            to=to,
            subject="Change password request",
            body="Click on the following link to change your password.\n\n" + url,
        )

    def execute(self, dto: RequestChangePasswordDTO) -> User:
        """
        Executes the use case to request a password change.

        Performs the following operations:
          1. Converts the email from the DTO into an Email object.
          2. Finds the user in the repository using the email.
          3. Generates a validation token for the user.
          4. Sends an email to the user with the link to change the password.
          5. Returns the corresponding User object.

        Args:
            dto (RequestChangePasswordDTO): Object containing the user's email and the
                                            base URL for the password change link.

        Returns:
            User: The User object found to which the email for password change was sent.
        """
        email = Email(dto.email)

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_email(email=email)
        )

        verify_token = self.__validation_token_repository.create_validation_request(
            user_uuid=user.uuid
        )

        self.__send_email(to=str(email), url=f"{dto.url}/{verify_token}")

        return user
