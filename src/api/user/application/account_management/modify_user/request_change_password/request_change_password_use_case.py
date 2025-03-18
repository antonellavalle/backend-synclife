from src.api.shared.domain.repositories.smtp_email_sender_repository import (
    SMTPEmailSenderRepository,
)
from src.api.user.application.account_management.modify_user.request_change_password.request_change_password_dto import (  # noqa: E501
    RequestChangePasswordDTO,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.repositories.validation_token_repository import (
    ValidationTokenRepository,
)
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects.email import Email


class RequestChangePasswordUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        smtp_email_sender_repository: SMTPEmailSenderRepository,
        validation_token_repository: ValidationTokenRepository,
    ) -> None:
        self.__user_repository = user_repository
        self.__smtp_email_sender_repository = smtp_email_sender_repository
        self.__validation_token_repository = validation_token_repository

    def __send_email(self, to: str, url: str) -> None:
        self.__smtp_email_sender_repository.send_email(
            to=to,
            subject="Change password request",
            body="Click on the following link to change your password.\n\n" + url,
        )

    def execute(self, dto: RequestChangePasswordDTO) -> None:
        email = Email(dto.email)

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_email(email=email)
        )

        verify_token = self.__validation_token_repository.create_validation_request(
            user_uuid=user.uuid
        )

        self.__send_email(to=str(email), url=f"{dto.url}/{verify_token}")
