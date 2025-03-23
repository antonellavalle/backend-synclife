from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.notes.domain.entities.note import Note
from src.api.notes.infrastructure.persistence.models.sqlmodel_note_tag_link_model import (  # noqa: E501
    SQLModelNoteTagModel,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_tag_model import (
    SQLModelTagModel,
)
from src.api.shared.domain.value_objects import Uuid
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class SQLModelNoteModel(SQLModel, table=True):
    __tablename__ = "note"

    uuid: str = Field(primary_key=True)
    user_uuid: str = Field(foreign_key="user.uuid")
    title: str
    content: str
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.today)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SQLModelUserModel" = Relationship(back_populates="notes")
    tags: List["SQLModelTagModel"] = Relationship(
        back_populates="notes", link_model=SQLModelNoteTagModel
    )

    @classmethod
    def from_entity(cls, entity: "Note") -> "SQLModelNoteModel":
        return cls(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            title=entity.title.strip(),
            content=entity.content.strip(),
            is_deleted=False,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> "Note":
        return Note(
            uuid=Uuid(uuid=self.uuid),
            user_uuid=Uuid(uuid=self.user_uuid),
            title=self.title,
            content=self.content,
            tags=[SQLModelTagModel.to_entity(self=tag) for tag in self.tags],
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
