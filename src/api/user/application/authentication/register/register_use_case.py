from datetime import datetime

from src.api.shared.domain.repositories.smtp_email_sender_repository import (
    SMTPEmailSenderRepository,
)
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.user.application.authentication.register.register_dto import RegisterDTO
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.repositories.validation_token_repository import (
    ValidationTokenRepository,
)
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects.email import Email
from src.api.user.domain.value_objects.full_name import FullName
from src.api.user.domain.value_objects.password import Password
from src.api.user.domain.value_objects.phone import Phone


class RegisterUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        smtp_email_sender_repository: SMTPEmailSenderRepository,
        validate_user_repository: ValidationTokenRepository,
    ) -> None:
        self.__user_repository = user_repository
        self.__smtp_email_sender_repository = smtp_email_sender_repository
        self.__validate_user_repository = validate_user_repository

    def __send_email(self, to: str, url: str) -> None:
        self.__smtp_email_sender_repository.send_email(
            to=to,
            subject="Validate account",
            body="Click on the following link to validate your account and finish the"
            " registration process.\n\n" + url,
        )

    def execute(self, dto: RegisterDTO) -> User:
        email = Email(email=dto.email)

        existing_user = self.__user_repository.find_by_email(
            email=email, include_deleted=True
        )
        if existing_user is not None:
            if existing_user.account_verified:
                raise UserRepositoryError(
                    error_type=UserRepositoryTypeError.ALREADY_EXISTS
                )
            else:
                verify_token = (
                    self.__validate_user_repository.create_validation_request(
                        user_uuid=existing_user.uuid
                    )
                )
                self.__send_email(to=str(email), url=f"{dto.url}/{verify_token}")
                return existing_user

        UserRepositoryValidator.is_email_already_registered(
            user_repository=self.__user_repository, email=email
        )

        user = User(
            uuid=Uuid(),
            email=email,
            password=Password(password=dto.password),
            full_name=FullName(first_name=dto.first_name, last_name=dto.last_name),
            birth_date=dto.birth_date,
            phone=Phone(phone=dto.phone),
            account_verified=False,
            is_deleted=False,
            created_at=datetime.now(),
            updated_at=None,
        )

        verify_token = self.__validate_user_repository.create_validation_request(
            user_uuid=user.uuid
        )
        self.__send_email(to=str(email), url=f"{dto.url}/{verify_token}")
        is_saved = self.__user_repository.save(user=user)

        if not is_saved:
            raise UserRepositoryError(
                error_type=UserRepositoryTypeError.OPERATION_FAILED
            )

        return user
