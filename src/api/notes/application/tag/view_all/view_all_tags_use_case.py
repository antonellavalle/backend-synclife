from typing import List

from src.api.notes.application.tag.view_all.view_all_tags_dto import ViewAllTagDTO
from src.api.notes.domain.entities.tag import Tag
from src.api.notes.domain.repositories.tag_repository import TagRepository
from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects.uuid import Uuid


class ViewAllTagUseCase:
    def __init__(
        self, tag_repository: TagRepository, session_repository: SessionRepository
    ):
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAllTagDTO) -> List[Tag]:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        tags = self.__tag_repository.find_all_by_user_uuid(
            user_uuid=Uuid(uuid=user_request_uuid)
        )

        return tags
