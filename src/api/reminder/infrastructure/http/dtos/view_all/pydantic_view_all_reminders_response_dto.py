from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from src.api.reminder.domain.entities.reminder import Reminder


@dataclass
class ReminderResponseType:
    uuid: str
    user_uuid: str
    title: str
    remind_date: datetime
    created_at: datetime
    updated_at: Optional[datetime]
    is_deleted: bool

    @staticmethod
    def from_entity(entity: Reminder) -> "ReminderResponseType":
        return ReminderResponseType(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            title=entity.title,
            remind_date=entity.remind_date,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            is_deleted=entity.is_deleted,
        )


class PydanticViewAllRemindersResponseDTO(BaseModel):
    items: List[ReminderResponseType]
