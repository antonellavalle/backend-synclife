from pydantic import BaseModel

from src.api.notes.application.tag.create_tag.create_tag_dto import CreateTagDTO


class PydanticCreateTagRequestDTO(BaseModel):
    user_id: str
    name: str

    def to_application(self, session_token: str) -> CreateTagDTO:
        return CreateTagDTO(
            user_id=self.user_id, name=self.name, session_token=session_token
        )
