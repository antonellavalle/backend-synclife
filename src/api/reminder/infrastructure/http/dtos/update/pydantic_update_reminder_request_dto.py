from datetime import datetime

from pydantic import BaseModel

from src.api.reminder.application.update.update_reminder_dto import UpdateReminderDTO


class PydanticUpdateReminderRequestDTO(BaseModel):
    reminder_uuid: str
    title: str
    remind_date: datetime

    def to_application(self, session_token: str) -> UpdateReminderDTO:
        return UpdateReminderDTO(
            reminder_uuid=self.reminder_uuid,
            title=self.title,
            remind_date=self.remind_date,
            session_token=session_token,
        )
