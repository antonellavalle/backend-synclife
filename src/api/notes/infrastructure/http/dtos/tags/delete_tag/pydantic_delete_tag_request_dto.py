from pydantic import BaseModel

from src.api.notes.application.tag.delete_tag.delete_tag_dto import DeleteTagDTO


class PydanticDeleteTagRequestDTO(BaseModel):
    tag_id: str

    def to_application(self, session_token: str) -> DeleteTagDTO:
        return DeleteTagDTO(tag_id=self.tag_id, session_token=session_token)
