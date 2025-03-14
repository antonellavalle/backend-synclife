from pydantic import BaseModel

from src.api.reminder.infrastructure.persistence.models import SQLModelReminderModel


class PydanticCreateReminderResponseDTO(BaseModel):
    item: SQLModelReminderModel
