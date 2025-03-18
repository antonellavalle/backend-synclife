from src.api.user.application.account_management.account_recovery.account_recovery_dto import (  # noqa: E501
    AccountRecoveryDTO,
)
from src.api.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.user.domain.errors.validate_token_repository_error import (
    ValidateTokenRepositoryError,
    ValidateTokenRepositoryTypeError,
)
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.repositories.validation_token_repository import (
    ValidationTokenRepository,
)
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class AccountRecoveryUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        validation_token_repository: ValidationTokenRepository,
    ) -> None:
        self.__user_repository = user_repository
        self.__validation_token_repository = validation_token_repository

    def execute(self, dto: AccountRecoveryDTO) -> None:
        user_uuid = (
            self.__validation_token_repository.find_user_from_validation_request(
                dto.validate_token
            )
        )

        if user_uuid is None:
            raise ValidateTokenRepositoryError(
                ValidateTokenRepositoryTypeError.INVALID_TOKEN
            )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(id=user_uuid, include_deleted=True)
        )

        user.is_deleted = False

        is_updated, user_updated = self.__user_repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)
