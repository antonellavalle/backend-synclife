from pydantic import BaseModel

from src.api.reminder.application.view.view_reminder_dto import ViewReminderDTO


class PydanticViewReminderRequestDTO(BaseModel):
    reminder_uuid: str

    def to_application(self, session_token: str) -> ViewReminderDTO:
        return ViewReminderDTO(
            reminder_uuid=self.reminder_uuid,
            session_token=session_token,
        )
