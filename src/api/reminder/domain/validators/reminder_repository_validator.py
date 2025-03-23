from typing import Optional

from src.api.reminder.domain.entities.reminder import Reminder
from src.api.reminder.domain.errors.reminder_repository_error import (
    ReminderRepositoryError,
    ReminderRepositoryTypeError,
)
from src.api.reminder.domain.repositories.reminder_repository import ReminderRepository
from src.api.shared.domain.value_objects.uuid import Uuid


class ReminderRepositoryValidator:
    @staticmethod
    def reminder_found(
        reminder: Optional[Reminder],
    ) -> Reminder:
        if reminder is None:
            raise ReminderRepositoryError(
                error_type=ReminderRepositoryTypeError.NOT_FOUND
            )
        return reminder

    @staticmethod
    def user_owns_reminder(
        reminder_repository: ReminderRepository,
        user_uuid: Uuid,
        reminder_uuid: Uuid,
    ) -> None:
        reminder = ReminderRepositoryValidator.reminder_found(
            reminder=reminder_repository.find_by_uuid(uuid=reminder_uuid)
        )
        if reminder.user_uuid != user_uuid:
            raise ReminderRepositoryError(
                error_type=ReminderRepositoryTypeError.NOT_OWNED_BY_USER
            )
