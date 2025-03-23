from src.api.notes.application.tag.delete.delete_tag_dto import DeleteTagDTO
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


class DeleteTagUseCase:
    def __init__(
        self, tag_repository: TagRepository, session_repository: SessionRepository
    ):
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: DeleteTagDTO) -> Tag:
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

        is_deleted, deleted_tag = self.__tag_repository.delete(tag=tag)
        if not is_deleted or deleted_tag is None:
            raise TagRepositoryError(error_type=TagRepositoryTypeError.OPERATION_FAILED)

        return deleted_tag
