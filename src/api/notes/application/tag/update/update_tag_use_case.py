from src.api.notes.application.tag.update.update_tag_dto import UpdateTagDTO
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


class UpdateTagUseCase:
    def __init__(
        self, tag_repository: TagRepository, session_repository: SessionRepository
    ) -> None:
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: UpdateTagDTO) -> Tag:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        tag_uuid = Uuid(uuid=dto.tag_uuid)
        tag = TagRepositoryValidator.tag_found(
            tag=self.__tag_repository.find_by_uuid(uuid=tag_uuid)
        )

        TagRepositoryValidator.user_owns_tag(
            tag_repository=self.__tag_repository,
            user_uuid=Uuid(uuid=user_request_uuid),
            tag_uuid=tag_uuid,
        )

        is_updated, updated_tag = self.__tag_repository.update(tag=tag)
        if not is_updated or updated_tag is None:
            raise TagRepositoryError(error_type=TagRepositoryTypeError.OPERATION_FAILED)

        return updated_tag
