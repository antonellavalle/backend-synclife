from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.user.application.account_management.modify_user.change_personal_information.change_personal_information_dto import (  # noqa: E501
    ChangePersonalInformationDTO,
)
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects.email import Email
from src.api.user.domain.value_objects.full_name import FullName
from src.api.user.domain.value_objects.phone import Phone


class ChangePersonalInformationUseCase:
    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: ChangePersonalInformationDTO) -> User:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        user = UserRepositoryValidator.user_found(
            user=self.__user_repository.find_by_uuid(uuid=Uuid(uuid=user_request_uuid))
        )

        user.email = Email(email=dto.email)
        user.full_name = FullName(first_name=dto.first_name, last_name=dto.last_name)
        user.birth_date = dto.birth_date
        user.phone = Phone(phone=dto.phone)

        is_updated, user_updated = self.__user_repository.update(user=user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(
                error_type=UserRepositoryTypeError.OPERATION_FAILED
            )

        return user_updated
