from typing import Tuple

from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.user.application.authentication.login.login_dto import LoginDTO
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors.user_validation_error import (
    UserValidationError,
    UserValidationTypeError,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects.email import Email


class LoginUseCase:
    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: LoginDTO) -> Tuple[User, str]:
        email = Email(email=dto.email)

        user = UserRepositoryValidator.user_found(
            user=self.__user_repository.find_by_email(email=email, validate=False),
            is_login=True,
        )

        if not user.password.check_password(plain_password=dto.password):
            raise UserValidationError(
                error_type=UserValidationTypeError.INVALID_CREDENTIALS
            )

        return user, self.__session_repository.create_session(user_uuid=user.uuid)
