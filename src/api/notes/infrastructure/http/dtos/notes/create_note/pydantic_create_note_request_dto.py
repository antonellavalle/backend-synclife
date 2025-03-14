from pydantic import BaseModel

from src.api.notes.application.note.create_note.create_note_dto import CreateNoteDTO


class PydanticCreateNoteRequestDTO(BaseModel):
    user_id: str
    title: str
    content: str

    def to_application(self, session_token: str) -> CreateNoteDTO:
        return CreateNoteDTO(
            user_id=self.user_id,
            title=self.title,
            content=self.content,
            session_token=session_token,
        )

    @classmethod
    def from_application(cls, app_dto: CreateNoteDTO) -> "PydanticCreateNoteRequestDTO":
        return cls(
            user_id=app_dto.user_id,
            title=app_dto.title,
            content=app_dto.content,
        )
