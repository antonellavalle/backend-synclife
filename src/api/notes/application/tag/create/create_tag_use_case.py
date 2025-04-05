from datetime import datetime

from src.api.notes.application.tag.create.create_tag_dto import CreateTagDTO
from src.api.notes.domain.entities.tag import Tag
from src.api.notes.domain.errors.tag.tag_repository_error import (
    TagRepositoryError,
    TagRepositoryTypeError,
)
from src.api.notes.domain.repositories.tag_repository import TagRepository
from src.api.notes.domain.validators.tag_repository_validator import (
    TagRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateTagUseCase:
    def __init__(
        self,
        tag_repository: TagRepository,
        user_repository: UserRepository,
        session_repository: SessionRepository,
    ):
        self.__tag_repository = tag_repository
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: CreateTagDTO) -> Tag:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        user = UserRepositoryValidator.user_found(
            user=self.__user_repository.find_by_uuid(uuid=Uuid(uuid=user_request_uuid))
        )

        UserRepositoryValidator.user_is_verified(user=user)

        TagRepositoryValidator.tag_name_unique(
            tag_repository=self.__tag_repository, name=dto.name, user_uuid=user.uuid
        )

        tag = Tag(
            uuid=Uuid(),
            user_uuid=user.uuid,
            name=dto.name.strip(),
            created_at=datetime.now(),
            updated_at=None,
            is_deleted=False,
        )

        is_saved = self.__tag_repository.save(tag=tag)

        if not is_saved:
            raise TagRepositoryError(error_type=TagRepositoryTypeError.OPERATION_FAILED)

        return tag
