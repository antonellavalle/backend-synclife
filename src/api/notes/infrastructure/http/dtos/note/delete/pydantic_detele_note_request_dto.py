from pydantic import BaseModel

from src.api.notes.application.note.delete.delete_note_dto import DeleteNoteDTO


class PydanticDeleteNoteRequestDTO(BaseModel):
    note_uuid: str

    def to_application(self, session_token: str) -> DeleteNoteDTO:
        return DeleteNoteDTO(note_uuid=self.note_uuid, session_token=session_token)
