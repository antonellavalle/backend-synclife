from dataclasses import dataclass


@dataclass
class ViewReminderDTO:
    reminder_uuid: str
    session_token: str
