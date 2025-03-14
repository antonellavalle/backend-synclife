from typing import List

from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SQLModelTagsModel,
)


class PydanticViewAllTagsResponseDTO(BaseModel):
    tags: List[SQLModelTagsModel]
