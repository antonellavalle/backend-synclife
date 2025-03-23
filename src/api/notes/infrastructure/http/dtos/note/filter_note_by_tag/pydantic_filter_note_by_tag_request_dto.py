from pydantic import BaseModel

from src.api.notes.application.note.filter_note_by_tag.filter_note_by_tag_dto import (  # noqa: E501
    FilterNotesByTagDTO,
)


class PydanticFilterNotesByTagRequestDTO(BaseModel):
    tag_uuid: str

    def to_application(self, session_token: str) -> FilterNotesByTagDTO:
        return FilterNotesByTagDTO(tag_uuid=self.tag_uuid, session_token=session_token)
