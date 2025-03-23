from pydantic import BaseModel

from src.api.notes.application.note.remove_tag.remove_tag_dto import RemoveTagDTO


class PydanticRemoveTagRequestDTO(BaseModel):
    note_uuid: str
    tag_uuid: str

    def to_application(self, session_token: str) -> RemoveTagDTO:
        return RemoveTagDTO(
            note_uuid=self.note_uuid,
            tag_uuid=self.tag_uuid,
            session_token=session_token,
        )
