from pydantic import BaseModel

from src.api.reminder.infrastructure.persistence.models import SQLModelReminderModel


class PydanticViewReminderResponseDTO(BaseModel):
    item: SQLModelReminderModel
