from datetime import datetime

from pydantic import BaseModel


class PydanticUpdateReminderResponseDTO(BaseModel):
    uuid: str
    title: str
    remind_date: datetime
