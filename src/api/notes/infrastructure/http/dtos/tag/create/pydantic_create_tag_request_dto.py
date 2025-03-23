from pydantic import BaseModel

from src.api.notes.application.tag.create.create_tag_dto import CreateTagDTO


class PydanticCreateTagRequestDTO(BaseModel):
    name: str

    def to_application(self, session_token: str) -> CreateTagDTO:
        return CreateTagDTO(name=self.name, session_token=session_token)
