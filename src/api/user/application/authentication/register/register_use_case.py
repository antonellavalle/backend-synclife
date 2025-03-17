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
