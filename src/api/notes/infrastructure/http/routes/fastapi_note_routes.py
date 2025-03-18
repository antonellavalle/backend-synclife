from fastapi import APIRouter, Header

from src.api.notes.infrastructure.http.controllers.notes.fastapi_notes_controller import (  # noqa: E501
    FastAPINotesController,
)
from src.api.notes.infrastructure.http.dtos.notes import (
    PydanticAddTagToNoteRequestDTO,
    PydanticAddTagToNoteResponseDTO,
    PydanticCreateNoteRequestDTO,
    PydanticCreateNoteResponseDTO,
    PydanticDeleteNotesRequestDTO,
    PydanticDeleteNotesResponseDTO,
    PydanticFilterNotesByTagRequestDTO,
    PydanticFilterNotesByTagResponseDTO,
    PydanticRemoveTagRequestDTO,
    PydanticRemoveTagResponseDTO,
    PydanticUpdateNotesRequestDTO,
    PydanticUpdateNotesResponseDTO,
    PydanticViewAllNotesResponseDTO,
    PydanticViewNotesRequestDTO,
    PydanticViewNotesResponseDTO,
)

router: APIRouter = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=PydanticCreateNoteResponseDTO)
async def create_note(
    dto: PydanticCreateNoteRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateNoteResponseDTO:
    return await FastAPINotesController.create(dto, session_token)


@router.get("/{note_id}", response_model=PydanticViewNotesResponseDTO)
async def view_note(
    dto: PydanticViewNotesRequestDTO,
    session_token: str = Header(...),
) -> PydanticViewNotesResponseDTO:
    return await FastAPINotesController.view(dto, session_token)


@router.get("/", response_model=PydanticViewAllNotesResponseDTO)
async def view_all_notes(
    session_token: str = Header(...),
) -> PydanticViewAllNotesResponseDTO:
    return await FastAPINotesController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateNotesResponseDTO)
async def update_nots(
    dto: PydanticUpdateNotesRequestDTO,
    session_token: str = Header(...),
) -> PydanticUpdateNotesResponseDTO:
    return await FastAPINotesController.update(dto, session_token)


@router.delete("/{note_id}", response_model=PydanticDeleteNotesResponseDTO)
async def delete_note(
    dto: PydanticDeleteNotesRequestDTO,
    session_token: str = Header(...),
) -> PydanticDeleteNotesResponseDTO:
    return await FastAPINotesController.delete(dto, session_token)


@router.post("/add_tag", response_model=PydanticAddTagToNoteResponseDTO)
async def add_tag_to_note(
    dto: PydanticAddTagToNoteRequestDTO,
    session_token: str = Header(...),
) -> PydanticAddTagToNoteResponseDTO:
    return await FastAPINotesController.add_tag_to_note(dto, session_token)


@router.get("/filter_by_tag", response_model=PydanticFilterNotesByTagResponseDTO)
async def filter_notes_by_tag(
    dto: PydanticFilterNotesByTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticFilterNotesByTagResponseDTO:
    return await FastAPINotesController.filter_notes_by_tag(dto, session_token)


@router.delete("/remove_tag", response_model=PydanticRemoveTagResponseDTO)
async def remove_tag_from_note(
    dto: PydanticRemoveTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticRemoveTagResponseDTO:
    return await FastAPINotesController.remove_tag_from_note(dto, session_token)
