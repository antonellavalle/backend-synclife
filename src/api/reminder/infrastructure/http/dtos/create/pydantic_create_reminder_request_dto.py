from datetime import datetime

from pydantic import BaseModel

from src.api.reminder.application.create.create_reminder_dto import CreateReminderDTO


class PydanticCreateReminderRequestDTO(BaseModel):
    title: str
    remind_date: datetime

    def to_application(self, session_token: str) -> CreateReminderDTO:
        return CreateReminderDTO(
            title=self.title,
            remind_date=self.remind_date,
            session_token=session_token,
        )
