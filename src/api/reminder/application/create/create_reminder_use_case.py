from datetime import datetime

from src.api.reminder.application.create.create_reminder_dto import CreateReminderDTO
from src.api.reminder.domain.entities.reminder import Reminder
from src.api.reminder.domain.errors.reminder_repository_error import (
    ReminderRepositoryError,
    ReminderRepositoryTypeError,
)
from src.api.reminder.domain.repositories.reminder_repository import ReminderRepository
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects.uuid import Uuid


class CreateReminderUseCase:
    def __init__(
        self,
        reminder_repository: ReminderRepository,
        session_repository: SessionRepository,
    ):
        self.__reminder_repository = reminder_repository
        self.__session_repository = session_repository

    def execute(self, dto: CreateReminderDTO) -> Reminder:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        reminder = Reminder(
            uuid=Uuid(),
            user_uuid=Uuid(uuid=user_request_uuid),
            title=dto.title,
            remind_date=dto.remind_date,
            created_at=datetime.now(),
            updated_at=None,
            is_deleted=False,
        )

        is_saved = self.__reminder_repository.save(reminder=reminder)
        if not is_saved:
            raise ReminderRepositoryError(
                error_type=ReminderRepositoryTypeError.OPERATION_FAILED
            )

        return reminder
