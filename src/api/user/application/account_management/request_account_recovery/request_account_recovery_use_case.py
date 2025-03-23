from src.api.shared.domain.repositories.smtp_email_sender_repository import (
    SMTPEmailSenderRepository,
)
from src.api.user.application.account_management.request_account_recovery.request_account_recovery_dto import (  # noqa: E501
    RequestAccountRecoveryDTO,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.repositories.validation_token_repository import (
    ValidationTokenRepository,
)
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects.email import Email


class RequestAccountRecoveryUseCase:
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
            subject="Account recovery request",
            body="Click on the following link to recover your account.\n\n" + url,
        )

    def execute(self, dto: RequestAccountRecoveryDTO) -> None:
        email = Email(email=dto.email)

        user = UserRepositoryValidator.user_found(
            user=self.__user_repository.find_by_email(email=email, include_deleted=True)
        )

        verify_token = self.__validation_token_repository.create_validation_request(
            user_uuid=user.uuid
        )

        self.__send_email(to=str(email), url=f"{dto.url}/{verify_token}")
