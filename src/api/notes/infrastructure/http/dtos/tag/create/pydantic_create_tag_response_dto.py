from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_tag_model import (
    SQLModelTagModel,
)


class PydanticCreateTagResponseDTO(BaseModel):
    tag: SQLModelTagModel
