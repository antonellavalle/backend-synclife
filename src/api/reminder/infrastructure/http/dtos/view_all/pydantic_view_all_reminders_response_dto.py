from typing import List

from pydantic import BaseModel

from src.api.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (  # noqa: E501
    SQLModelReminderModel,
)


class PydanticViewAllRemindersResponseDTO(BaseModel):
    items: List[SQLModelReminderModel]
