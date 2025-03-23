from pydantic import BaseModel

from src.api.notes.application.tag.view.view_tag_dto import ViewTagDTO


class PydanticViewTagRequestDTO(BaseModel):
    tag_uuid: str

    def to_application(self, session_token: str) -> ViewTagDTO:
        return ViewTagDTO(tag_uuid=self.tag_uuid, session_token=session_token)
