from datetime import datetime

from pydantic import BaseModel


class PydanticViewReminderResponseDTO(BaseModel):
    uuid: str
    title: str
    remind_date: datetime
