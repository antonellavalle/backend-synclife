from src.api.notes.application.note.delete.delete_note_dto import DeleteNoteDTO
from src.api.notes.domain.entities.note import Note
from src.api.notes.domain.errors.note.note_repository_error import (
    NoteRepositoryError,
    NoteRepositoryTypeError,
)
from src.api.notes.domain.repositories.note_repository import NoteRepository
from src.api.notes.domain.validators.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class DeleteNoteUseCase:
    def __init__(
        self, note_repository: NoteRepository, session_repository: SessionRepository
    ):
        self.__note_repository = note_repository
        self.__session_repository = session_repository

    def execute(self, dto: DeleteNoteDTO) -> Note:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        note_uuid = Uuid(uuid=dto.note_uuid)
        note = NotesRepositoryValidator.note_found(
            note=self.__note_repository.find_by_uuid(uuid=note_uuid)
        )

        NotesRepositoryValidator.user_owns_note(
            note_repository=self.__note_repository,
            user_uuid=Uuid(uuid=user_request_uuid),
            note_uuid=note_uuid,
        )

        is_deleted, deleted_note = self.__note_repository.delete(note=note)
        if not is_deleted or deleted_note is None:
            raise NoteRepositoryError(
                error_type=NoteRepositoryTypeError.OPERATION_FAILED
            )
        return deleted_note
