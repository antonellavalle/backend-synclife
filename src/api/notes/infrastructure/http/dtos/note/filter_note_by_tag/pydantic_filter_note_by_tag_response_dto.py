from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from src.api.notes.domain.entities.note import Note
from src.api.notes.infrastructure.http.dtos.tag.view_all.pydantic_view_all_tags_response_dto import (  # noqa: E501
    TagResponseType,
)


@dataclass
class FilterNotesByTagResponseType:
    uuid: str
    user_uuid: str
    title: str
    content: str
    tags: List[TagResponseType]
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime]

    @staticmethod
    def from_entity(entity: Note) -> "FilterNotesByTagResponseType":
        tags_entities = [TagResponseType.from_entity(tag) for tag in entity.tags]
        return FilterNotesByTagResponseType(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            title=entity.title,
            content=entity.content,
            tags=tags_entities,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


class PydanticFilterNotesByTagResponseDTO(BaseModel):
    notes: List[FilterNotesByTagResponseType]
