from typing import List

from src.api.notes.application.note.filter_note_by_tag.filter_note_by_tag_dto import (  # noqa: E501
    FilterNotesByTagDTO,
)
from src.api.notes.domain.entities.note import Note
from src.api.notes.domain.repositories.note_repository import NoteRepository
from src.api.notes.domain.repositories.tag_repository import TagRepository
from src.api.notes.domain.validators.tag_repository_validator import (
    TagRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects.uuid import Uuid


class FilterNotesByTagUseCase:
    def __init__(
        self,
        note_repository: NoteRepository,
        tag_repository: TagRepository,
        session_repository: SessionRepository,
    ):
        self.__note_repository = note_repository
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: FilterNotesByTagDTO) -> List[Note]:
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
            user_uuid=Uuid(user_request_uuid),
            tag_uuid=tag_uuid,
        )

        # Filtra las notas por el tagsillo
        notes = self.__note_repository.find_by_tag(tag_uuid=tag.uuid)

        return notes
