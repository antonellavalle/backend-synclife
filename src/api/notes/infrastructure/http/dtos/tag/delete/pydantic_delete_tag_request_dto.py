from pydantic import BaseModel

from src.api.notes.application.tag.delete.delete_tag_dto import DeleteTagDTO


class PydanticDeleteTagRequestDTO(BaseModel):
    tag_uuid: str

    def to_application(self, session_token: str) -> DeleteTagDTO:
        return DeleteTagDTO(tag_uuid=self.tag_uuid, session_token=session_token)
