from pydantic import BaseModel

from src.api.notes.application.note.view.view_note_dto import ViewNoteDTO


class PydanticViewNoteRequestDTO(BaseModel):
    note_uuid: str

    def to_application(self, session_token: str) -> ViewNoteDTO:
        return ViewNoteDTO(note_uuid=self.note_uuid, session_token=session_token)
