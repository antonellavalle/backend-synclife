from src.api.notes.application.note.add_tags.add_tags_dto import AddTagsDTO
from src.api.notes.domain.entities.note import Note
from src.api.notes.domain.errors.note.note_repository_error import (
    NoteRepositoryError,
    NoteRepositoryTypeError,
)
from src.api.notes.domain.repositories.note_repository import NoteRepository
from src.api.notes.domain.repositories.tag_repository import TagRepository
from src.api.notes.domain.validators.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.notes.domain.validators.tag_repository_validator import (
    TagRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects.uuid import Uuid


class AddTagsUseCase:
    def __init__(
        self,
        note_repository: NoteRepository,
        tag_repository: TagRepository,
        session_repository: SessionRepository,
    ):
        self.__note_repository = note_repository
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: AddTagsDTO) -> Note:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        note_uuid = Uuid(uuid=dto.note_uuid)
        user_request_uuid = Uuid(uuid=user_request_uuid)

        note = NotesRepositoryValidator.note_found(
            note=self.__note_repository.find_by_uuid(uuid=note_uuid)
        )

        NotesRepositoryValidator.user_owns_note(
            note_repository=self.__note_repository,
            user_uuid=user_request_uuid,
            note_uuid=note_uuid,
        )

        # Valida los tags
        for tag_id in dto.tags:
            tag = TagRepositoryValidator.tag_found(
                tag=self.__tag_repository.find_by_uuid(uuid=Uuid(uuid=tag_id))
            )

            TagRepositoryValidator.user_owns_tag(
                tag_repository=self.__tag_repository,
                user_uuid=user_request_uuid,
                tag_uuid=tag.uuid,
            )

            # Agrega el tagsillo a la notita
            note.add_tag(tag=tag)

        # Actualiza la nota
        is_updated, updated_note = self.__note_repository.update(note=note)
        if not is_updated or updated_note is None:
            raise NoteRepositoryError(
                error_type=NoteRepositoryTypeError.OPERATION_FAILED
            )

        return updated_note
