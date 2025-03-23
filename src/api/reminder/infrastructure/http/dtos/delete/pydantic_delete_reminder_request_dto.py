from pydantic import BaseModel

from src.api.reminder.application.delete.delete_reminder_dto import DeleteReminderDTO


class PydanticDeleteReminderRequestDTO(BaseModel):
    reminder_uuid: str

    def to_application(self, session_token: str) -> DeleteReminderDTO:
        return DeleteReminderDTO(
            reminder_uuid=self.reminder_uuid, session_token=session_token
        )
