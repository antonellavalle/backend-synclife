from dataclasses import dataclass


@dataclass
class DeleteReminderDTO:
    reminder_uuid: str
    session_token: str
