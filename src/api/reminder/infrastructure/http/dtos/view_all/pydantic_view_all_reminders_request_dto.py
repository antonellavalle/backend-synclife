from pydantic import BaseModel

from src.api.reminder.application.view_all.view_all_reminders_dto import (
    ViewAllRemindersDTO,
)


class PydanticViewAllRemindersRequestDTO(BaseModel):
    def to_application(self, session_token: str) -> ViewAllRemindersDTO:
        return ViewAllRemindersDTO(
            session_token=session_token,
        )
