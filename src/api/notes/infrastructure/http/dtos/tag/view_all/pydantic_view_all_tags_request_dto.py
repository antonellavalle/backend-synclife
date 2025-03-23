from pydantic import BaseModel

from src.api.notes.application.tag.view_all.view_all_tags_dto import ViewAllTagDTO


class PydanticViewAllTagsRequestDTO(BaseModel):
    def to_application(self, session_token: str) -> ViewAllTagDTO:
        return ViewAllTagDTO(session_token=session_token)
