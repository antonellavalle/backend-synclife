from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreateReminderDTO:
    title: str
    remind_date: datetime
    session_token: str
