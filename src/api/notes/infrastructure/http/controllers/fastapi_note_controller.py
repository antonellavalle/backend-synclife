from src.api.notes.application.note.add_tags.add_tags_use_case import AddTagsUseCase
from src.api.notes.application.note.create.create_note_use_case import CreateNoteUseCase
from src.api.notes.application.note.delete.delete_note_use_case import DeleteNoteUseCase
from src.api.notes.application.note.filter_note_by_tag.filter_note_by_tag_use_case import (  # noqa: E501
    FilterNotesByTagUseCase,
)
from src.api.notes.application.note.remove_tag.remove_tag_use_case import (
    RemoveTagUseCase,
)
from src.api.notes.application.note.update.update_note_use_case import UpdateNoteUseCase
from src.api.notes.application.note.view.view_note_use_case import ViewNoteUseCase
from src.api.notes.application.note.view_all_notes.view_all_notes_use_case import (
    ViewAllNotesUseCase,
)
from src.api.notes.infrastructure.http.dtos.note.add_tags.pydantic_add_tags_request_dto import (  # noqa: E501
    PydanticAddTagsRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.add_tags.pydantic_add_tags_response_dto import (  # noqa: E501
    PydanticAddTagsResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.create.pydantic_create_note_request_dto import (  # noqa: E501
    PydanticCreateNoteRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.create.pydantic_create_note_response_dto import (  # noqa: E501
    PydanticCreateNoteResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.delete.pydantic_delete_note_response_dto import (  # noqa: E501
    PydanticDeleteNoteResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.delete.pydantic_detele_note_request_dto import (  # noqa: E501
    PydanticDeleteNoteRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.filter_note_by_tag.pydantic_filter_note_by_tag_request_dto import (  # noqa: E501
    PydanticFilterNotesByTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.filter_note_by_tag.pydantic_filter_note_by_tag_response_dto import (  # noqa: E501
    FilterNotesByTagResponseType,
    PydanticFilterNotesByTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.remove_tag.pydantic_remove_tag_request_dto import (  # noqa: E501
    PydanticRemoveTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.remove_tag.pydantic_remove_tag_response_dto import (  # noqa: E501
    PydanticRemoveTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.update.pydantic_update_note_request_dto import (  # noqa: E501
    PydanticUpdateNoteRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.update.pydantic_update_note_response_dto import (  # noqa: E501
    PydanticUpdateNoteResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.view.pydantic_view_note_request_dto import (  # noqa: E501
    PydanticViewNoteRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.view.pydantic_view_note_response_dto import (  # noqa: E501
    PydanticViewNoteResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.view_all.pydantic_view_all_notes_request_dto import (  # noqa: E501
    PydanticViewAllNotesRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.note.view_all.pydantic_view_all_notes_response_dto import (  # noqa: E501
    NoteResponseType,
    PydanticViewAllNotesResponseDTO,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_note_model import (
    SQLModelNoteModel,
)
from src.api.notes.infrastructure.persistence.repositories.sqlmodel_note_repository import (  # noqa: E501
    SQLModelNoteRepository,
)
from src.api.notes.infrastructure.persistence.repositories.sqlmodel_tag_repository import (  # noqa: E501
    SQLModelTagRepository,
)
from src.api.shared.infrastructure.http.decorators.handle_exceptions import (
    handle_exceptions,
)
from src.api.shared.infrastructure.persistence.repositories.dragonfly_session_repository import (  # noqa: E501
    DragonflySessionRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SQLModelUserRepository,
)


class FastAPINotesController:
    @staticmethod
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateNoteRequestDTO, session_token: str
    ) -> PydanticCreateNoteResponseDTO:
        note_repo = SQLModelNoteRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = CreateNoteUseCase(
            note_repository=note_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        app_dto = request_dto.to_application(session_token=session_token)

        note = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticCreateNoteResponseDTO(
            note=SQLModelNoteModel.from_entity(entity=note)
        )

    @staticmethod
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateNoteRequestDTO, session_token: str
    ) -> PydanticUpdateNoteResponseDTO:
        note_repo = SQLModelNoteRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = UpdateNoteUseCase(
            note_repository=note_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = request_dto.to_application(session_token=session_token)

        updated_note = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticUpdateNoteResponseDTO(
            note=SQLModelNoteModel.from_entity(entity=updated_note)
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        reques_dto: PydanticDeleteNoteRequestDTO, session_token: str
    ) -> PydanticDeleteNoteResponseDTO:
        note_repo = SQLModelNoteRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = DeleteNoteUseCase(
            note_repository=note_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = reques_dto.to_application(session_token=session_token)

        deleted_note = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticDeleteNoteResponseDTO(
            note=SQLModelNoteModel.from_entity(entity=deleted_note)
        )

    @staticmethod
    @handle_exceptions
    async def view(note_uuid: str, session_token: str) -> PydanticViewNoteResponseDTO:
        note_repo = SQLModelNoteRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewNoteUseCase(
            note_repository=note_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = PydanticViewNoteRequestDTO(note_uuid=note_uuid).to_application(
            session_token=session_token
        )

        note = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticViewNoteResponseDTO(
            note=SQLModelNoteModel.from_entity(entity=note)
        )

    @staticmethod
    @handle_exceptions
    async def view_all(session_token: str) -> PydanticViewAllNotesResponseDTO:
        note_repo = SQLModelNoteRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewAllNotesUseCase(
            note_repository=note_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = PydanticViewAllNotesRequestDTO().to_application(
            session_token=session_token
        )

        notes = use_case.execute(dto=dto)

        response_notes = [NoteResponseType.from_entity(entity=note) for note in notes]

        # TODO: optimizar response
        return PydanticViewAllNotesResponseDTO(notes=response_notes)

    @staticmethod
    @handle_exceptions
    async def add_tags(
        request_dto: PydanticAddTagsRequestDTO, session_token: str
    ) -> PydanticAddTagsResponseDTO:
        notes_repo = SQLModelNoteRepository.get_repository()
        tag_repo = SQLModelTagRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = AddTagsUseCase(
            note_repository=notes_repo,
            tag_repository=tag_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = request_dto.to_application(session_token=session_token)

        note = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticAddTagsResponseDTO(
            note=SQLModelNoteModel.from_entity(entity=note)
        )

    @staticmethod
    @handle_exceptions
    async def remove_tag(
        remove_data: PydanticRemoveTagRequestDTO, session_token: str
    ) -> PydanticRemoveTagResponseDTO:
        notes_repo = SQLModelNoteRepository.get_repository()
        tag_repo = SQLModelTagRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = RemoveTagUseCase(
            note_repository=notes_repo,
            tag_repository=tag_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = remove_data.to_application(session_token=session_token)

        updated_note = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticRemoveTagResponseDTO(
            note=SQLModelNoteModel.from_entity(entity=updated_note)
        )

    @staticmethod
    @handle_exceptions
    async def filter_notes_by_tag(
        tag_uuid: str, session_token: str
    ) -> PydanticFilterNotesByTagResponseDTO:
        notes_repo = SQLModelNoteRepository.get_repository()
        tag_repo = SQLModelTagRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = FilterNotesByTagUseCase(
            note_repository=notes_repo,
            tag_repository=tag_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = PydanticFilterNotesByTagRequestDTO(tag_uuid=tag_uuid).to_application(
            session_token=session_token
        )

        notes = use_case.execute(dto=dto)

        response_notes = [
            FilterNotesByTagResponseType.from_entity(entity=note) for note in notes
        ]

        # TODO: optimizar response
        return PydanticFilterNotesByTagResponseDTO(notes=response_notes)
