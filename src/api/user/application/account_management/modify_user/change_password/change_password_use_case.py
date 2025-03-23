from src.api.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDTO,
)
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
from src.api.user.domain.value_objects.password import Password


class ChangePasswordUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        validation_token_repository: ValidationTokenRepository,
    ) -> None:
        self.__user_repository = user_repository
        self.__validation_token_repository = validation_token_repository

    def execute(self, dto: ChangePasswordDTO) -> None:
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

        user.password = Password(password=dto.new_password)

        is_updated, user_updated = self.__user_repository.update(user=user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(
                error_type=UserRepositoryTypeError.OPERATION_FAILED
            )
