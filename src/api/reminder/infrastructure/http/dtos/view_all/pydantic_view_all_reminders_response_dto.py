from dataclasses import dataclass
from datetime import datetime
from typing import List

from pydantic import BaseModel


@dataclass
class ReminderResponseType:
    uuid: str
    title: str
    remind_date: datetime


class PydanticViewAllRemindersResponseDTO(BaseModel):
    items: List[ReminderResponseType]
