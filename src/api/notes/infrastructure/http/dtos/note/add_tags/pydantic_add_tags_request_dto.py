from typing import List

from pydantic import BaseModel

from src.api.notes.application.note.add_tags.add_tags_dto import AddTagsDTO


class PydanticAddTagsRequestDTO(BaseModel):
    note_uuid: str
    tags: List[str]

    def to_application(self, session_token: str) -> AddTagsDTO:
        return AddTagsDTO(
            note_uuid=self.note_uuid, tags=self.tags, session_token=session_token
        )
