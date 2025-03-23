from pydantic import BaseModel

from src.api.notes.application.note.create.create_note_dto import CreateNoteDTO


class PydanticCreateNoteRequestDTO(BaseModel):
    title: str
    content: str

    def to_application(self, session_token: str) -> CreateNoteDTO:
        return CreateNoteDTO(
            title=self.title,
            content=self.content,
            session_token=session_token,
        )
