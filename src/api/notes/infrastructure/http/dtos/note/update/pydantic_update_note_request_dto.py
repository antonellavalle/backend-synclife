from pydantic import BaseModel

from src.api.notes.application.note.update.update_note_dto import UpdateNoteDTO


class PydanticUpdateNoteRequestDTO(BaseModel):
    note_uuid: str
    title: str
    content: str

    def to_application(self, session_token: str) -> UpdateNoteDTO:
        return UpdateNoteDTO(
            note_uuid=self.note_uuid,
            title=self.title,
            content=self.content,
            session_token=session_token,
        )
