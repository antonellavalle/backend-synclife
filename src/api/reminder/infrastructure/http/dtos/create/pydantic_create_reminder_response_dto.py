from datetime import datetime

from pydantic import BaseModel


class PydanticCreateReminderResponseDTO(BaseModel):
    uuid: str
    title: str
    remind_date: datetime
