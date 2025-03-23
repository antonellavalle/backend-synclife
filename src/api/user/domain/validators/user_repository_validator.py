from typing import Optional

from src.api.user.domain.entities.user import User
from src.api.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.user.domain.errors.user_validation_error import (
    UserValidationError,
    UserValidationTypeError,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.value_objects.email import Email


class UserRepositoryValidator:
    @staticmethod
    def is_email_already_registered(
        user_repository: UserRepository, email: Email
    ) -> None:
        existing_user = user_repository.find_by_email(email=email, include_deleted=True)
        if existing_user is not None:
            raise UserRepositoryError(
                error_type=UserRepositoryTypeError.USER_ALREADY_EXISTS
            )

    @staticmethod
    def user_found(user: Optional[User], is_login: bool = False) -> User:
        if user is None:
            if is_login:
                raise UserValidationError(
                    error_type=UserValidationTypeError.INVALID_CREDENTIALS
                )
            else:
                raise UserRepositoryError(
                    error_type=UserRepositoryTypeError.USER_NOT_FOUND
                )
        return user
