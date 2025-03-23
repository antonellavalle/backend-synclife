from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.reminder.domain.entities.reminder import Reminder
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class SQLModelReminderModel(SQLModel, table=True):
    __tablename__ = "reminder"

    uuid: str = Field(primary_key=True, nullable=False, max_length=36)
    user_uuid: str = Field(foreign_key="user.uuid", nullable=False, max_length=36)
    title: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    remind_date: datetime = Field(nullable=False)
    is_deleted: bool = Field(default=False, nullable=False)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SQLModelUserModel" = Relationship(back_populates="reminder_items")

    @classmethod
    def from_entity(cls, entity: "Reminder") -> "SQLModelReminderModel":
        return cls(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            title=entity.title,
            remind_date=entity.remind_date,
            updated_at=entity.updated_at,
            created_at=entity.created_at,
            is_deleted=entity.is_deleted,
        )

    def to_entity(self) -> "Reminder":
        return Reminder(
            uuid=Uuid(self.uuid),
            user_uuid=Uuid(self.user_uuid),
            title=self.title,
            remind_date=self.remind_date,
            updated_at=self.updated_at,
            created_at=self.created_at,
            is_deleted=self.is_deleted,
        )
