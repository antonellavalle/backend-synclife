from fastapi import APIRouter, Header

from src.api.notes.infrastructure.http.controllers.fastapi_note_controller import (  # noqa: E501
    FastAPINotesController,
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
from src.api.notes.infrastructure.http.dtos.note.view.pydantic_view_note_response_dto import (  # noqa: E501
    PydanticViewNoteResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.note.view_all.pydantic_view_all_notes_response_dto import (  # noqa: E501
    PydanticViewAllNotesResponseDTO,
)

router: APIRouter = APIRouter(prefix="/note", tags=["Notes"])


@router.post("/", response_model=PydanticCreateNoteResponseDTO)
async def create_note(
    dto: PydanticCreateNoteRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateNoteResponseDTO:
    return await FastAPINotesController.create(dto, session_token)


@router.get("/{note_uuid}", response_model=PydanticViewNoteResponseDTO)
async def view_note(
    note_uuid: str,
    session_token: str = Header(...),
) -> PydanticViewNoteResponseDTO:
    return await FastAPINotesController.view(note_uuid, session_token)


@router.get("/", response_model=PydanticViewAllNotesResponseDTO)
async def view_all_notes(
    session_token: str = Header(...),
) -> PydanticViewAllNotesResponseDTO:
    return await FastAPINotesController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateNoteResponseDTO)
async def update_note(
    dto: PydanticUpdateNoteRequestDTO,
    session_token: str = Header(...),
) -> PydanticUpdateNoteResponseDTO:
    return await FastAPINotesController.update(dto, session_token)


@router.delete("/", response_model=PydanticDeleteNoteResponseDTO)
async def delete_note(
    dto: PydanticDeleteNoteRequestDTO,
    session_token: str = Header(...),
) -> PydanticDeleteNoteResponseDTO:
    return await FastAPINotesController.delete(dto, session_token)


@router.post("/add-tags", response_model=PydanticAddTagsResponseDTO)
async def add_tags_to_note(
    dto: PydanticAddTagsRequestDTO,
    session_token: str = Header(...),
) -> PydanticAddTagsResponseDTO:
    return await FastAPINotesController.add_tags(dto, session_token)


@router.get("/filter-by-tag", response_model=PydanticFilterNotesByTagResponseDTO)
async def filter_notes_by_tag(
    dto: PydanticFilterNotesByTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticFilterNotesByTagResponseDTO:
    return await FastAPINotesController.filter_notes_by_tag(dto, session_token)


@router.delete("/remove-tag", response_model=PydanticRemoveTagResponseDTO)
async def remove_tag_from_note(
    dto: PydanticRemoveTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticRemoveTagResponseDTO:
    return await FastAPINotesController.remove_tag(dto, session_token)
