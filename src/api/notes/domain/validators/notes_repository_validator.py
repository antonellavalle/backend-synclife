from typing import Optional

from src.api.notes.domain.entities.note import Note
from src.api.notes.domain.errors.note.note_repository_error import (
    NoteRepositoryError,
    NoteRepositoryTypeError,
)
from src.api.notes.domain.repositories.note_repository import NoteRepository
from src.api.shared.domain.value_objects.uuid import Uuid


class NotesRepositoryValidator:
    @staticmethod
    def note_found(note: Optional[Note]) -> Note:
        if note is None:
            raise NoteRepositoryError(error_type=NoteRepositoryTypeError.NOT_FOUND)
        return note

    @staticmethod
    def user_owns_note(
        note_repository: NoteRepository, user_uuid: Uuid, note_uuid: Uuid
    ) -> None:
        note = note_repository.find_by_uuid(uuid=note_uuid)
        if note is None or note.user_uuid != user_uuid:
            raise NoteRepositoryError(error_type=NoteRepositoryTypeError.NOT_OWNED)

    @staticmethod
    def note_title_unique(
        note_repository: NoteRepository, title: str, user_uuid: Uuid
    ) -> None:
        if note_repository.find_by_title_and_user_uuid(
            title=title, user_uuid=user_uuid
        ):
            raise NoteRepositoryError(
                error_type=NoteRepositoryTypeError.DUPLICATED_TITLE
            )
