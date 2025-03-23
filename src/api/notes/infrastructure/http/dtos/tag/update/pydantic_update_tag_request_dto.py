from pydantic import BaseModel

from src.api.notes.application.tag.update.update_tag_dto import UpdateTagDTO


class PydanticUpdateTagRequestDTO(BaseModel):
    tag_uuid: str
    name: str

    def to_application(self, session_token: str) -> UpdateTagDTO:
        return UpdateTagDTO(
            tag_uuid=self.tag_uuid, name=self.name, session_token=session_token
        )
