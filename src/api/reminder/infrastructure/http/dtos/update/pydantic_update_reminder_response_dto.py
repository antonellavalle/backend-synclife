from pydantic import BaseModel

from src.api.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (
    SQLModelReminderModel,
)


class PydanticUpdateReminderResponseDTO(BaseModel):
    reminder: SQLModelReminderModel
