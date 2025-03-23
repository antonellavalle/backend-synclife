from typing import List

from src.api.notes.application.note.view_all_notes.view_all_notes_dto import (
    ViewAllNotesDTO,
)
from src.api.notes.domain.entities.note import Note
from src.api.notes.domain.repositories.note_repository import NoteRepository
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects.uuid import Uuid


class ViewAllNotesUseCase:
    def __init__(
        self, note_repository: NoteRepository, session_repository: SessionRepository
    ):
        self.__note_repository = note_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAllNotesDTO) -> List[Note]:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        note = self.__note_repository.find_all_by_user_uuid(
            user_uuid=Uuid(uuid=user_request_uuid)
        )

        return note
