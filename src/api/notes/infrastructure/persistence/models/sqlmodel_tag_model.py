from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.notes.domain.entities.tag import Tag
from src.api.notes.infrastructure.persistence.models.sqlmodel_note_tag_link_model import (  # noqa: E501
    SQLModelNoteTagModel,
)
from src.api.shared.domain.value_objects.uuid import Uuid

if TYPE_CHECKING:
    from src.api.notes.infrastructure.persistence.models.sqlmodel_note_model import (  # noqa: E501
        SQLModelNoteModel,
    )
    from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
        SQLModelUserModel,
    )


class SQLModelTagModel(SQLModel, table=True):
    __tablename__ = "tag"

    uuid: str = Field(primary_key=True)
    user_uuid: str = Field(foreign_key="user.uuid")
    name: str
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.today)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SQLModelUserModel" = Relationship(back_populates="tags")
    notes: List["SQLModelNoteModel"] = Relationship(
        back_populates="tags", link_model=SQLModelNoteTagModel
    )

    @classmethod
    def from_entity(cls, entity: "Tag") -> "SQLModelTagModel":
        return cls(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            name=entity.name.strip(),
            is_deleted=False,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> "Tag":
        return Tag(
            uuid=Uuid(uuid=self.uuid),
            user_uuid=Uuid(uuid=self.user_uuid),
            name=self.name,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
