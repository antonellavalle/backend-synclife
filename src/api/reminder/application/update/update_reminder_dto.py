from dataclasses import dataclass
from datetime import datetime


@dataclass
class UpdateReminderDTO:
    reminder_uuid: str
    title: str
    remind_date: datetime
    session_token: str
