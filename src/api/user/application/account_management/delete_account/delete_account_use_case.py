from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects import Uuid
from src.api.user.application.account_management.delete_account.delete_account_dto import (  # noqa: E501
    DeleteAccountDTO,
)
from src.api.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class DeleteAccountUseCase:
    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: DeleteAccountDTO) -> None:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(Uuid(user_request_uuid))
        )

        is_deleted, user_deleted = self.__user_repository.delete(user)

        if not is_deleted or user_deleted is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)
