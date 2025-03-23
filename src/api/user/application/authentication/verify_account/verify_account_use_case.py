from typing import Tuple

from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.user.application.authentication.verify_account.verify_account_dto import (
    VerifyAccountDTO,
)
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.user.domain.errors.validate_token_repository_error import (
    ValidateTokenRepositoryError,
    ValidateTokenRepositoryTypeError,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.repositories.validation_token_repository import (
    ValidationTokenRepository,
)
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class VerifyAccountUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        validation_token_repository: ValidationTokenRepository,
        session_repository: SessionRepository,
    ) -> None:
        self.__user_repository = user_repository
        self.__validation_token_repository = validation_token_repository
        self.__session_repository = session_repository

    def execute(self, dto: VerifyAccountDTO) -> Tuple[User, str]:
        user_uuid = (
            self.__validation_token_repository.find_user_from_validation_request(
                validation_token=dto.validate_token
            )
        )

        if user_uuid is None:
            raise ValidateTokenRepositoryError(
                error_type=ValidateTokenRepositoryTypeError.INVALID_TOKEN
            )

        user = UserRepositoryValidator.user_found(
            user=self.__user_repository.find_by_uuid(uuid=user_uuid)
        )

        if user.account_verified:
            raise ValidateTokenRepositoryError(
                error_type=ValidateTokenRepositoryTypeError.ALREADY_VERIFIED
            )

        user.account_verified = True

        is_updated, user_updated = self.__user_repository.update(user=user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(
                error_type=UserRepositoryTypeError.OPERATION_FAILED
            )

        return user, self.__session_repository.create_session(
            user_uuid=user_updated.uuid
        )
