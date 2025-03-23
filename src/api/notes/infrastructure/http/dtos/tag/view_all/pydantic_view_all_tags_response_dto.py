from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from src.api.notes.domain.entities.tag import Tag


@dataclass
class TagResponseType:
    uuid: str
    user_uuid: str
    name: str
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime]

    @staticmethod
    def from_entity(entity: Tag) -> "TagResponseType":
        return TagResponseType(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            name=entity.name,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


class PydanticViewAllTagsResponseDTO(BaseModel):
    tags: List[TagResponseType]
