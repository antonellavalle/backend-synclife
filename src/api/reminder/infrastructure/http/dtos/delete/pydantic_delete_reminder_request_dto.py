from pydantic import BaseModel

from src.api.reminder.application.delete import DeleteReminderDTO


class PydanticDeleteReminderRequestDTO(BaseModel):
    reminder_uuid: str

    def to_application(self, session_token: str) -> DeleteReminderDTO:
        return DeleteReminderDTO(
            reminder_uuid=self.reminder_uuid, session_token=session_token
        )
