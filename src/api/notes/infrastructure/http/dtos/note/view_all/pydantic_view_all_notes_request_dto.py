from pydantic import BaseModel

from src.api.notes.application.note.view_all_notes.view_all_notes_dto import (
    ViewAllNotesDTO,
)


class PydanticViewAllNotesRequestDTO(BaseModel):
    def to_application(self, session_token: str) -> ViewAllNotesDTO:
        return ViewAllNotesDTO(session_token=session_token)
