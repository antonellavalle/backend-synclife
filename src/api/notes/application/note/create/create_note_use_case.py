from datetime import datetime

from src.api.notes.application.note.create.create_note_dto import CreateNoteDTO
from src.api.notes.domain.entities.note import Note
from src.api.notes.domain.repositories.note_repository import NoteRepository
from src.api.notes.domain.validators.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class CreateNoteUseCase:
    def __init__(
        self,
        note_repository: NoteRepository,
        session_repository: SessionRepository,
    ):
        self.__note_repository = note_repository
        self.__session_repository = session_repository

    def execute(self, dto: CreateNoteDTO) -> Note:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        user_uuid = Uuid(uuid=user_request_uuid)
        NotesRepositoryValidator.note_title_unique(
            note_repository=self.__note_repository, title=dto.title, user_uuid=user_uuid
        )

        note = Note(
            uuid=Uuid(),
            user_uuid=user_uuid,
            title=dto.title.strip(),
            content=dto.content.strip(),
            created_at=datetime.now(),
            updated_at=None,
            is_deleted=False,
            tags=[],
        )

        self.__note_repository.save(note=note)
        return note
