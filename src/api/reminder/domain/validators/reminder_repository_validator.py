from typing import Optional

from src.api.reminder.domain.entities.reminder import Reminder
from src.api.reminder.domain.errors import (
    ReminderRepositoryError,
    ReminderRepositoryTypeError,
)
from src.api.reminder.domain.repositories.reminder_repository import ReminderRepository
from src.api.shared.domain.value_objects import Uuid


class ReminderRepositoryValidator:
    @staticmethod
    def reminder_found(
        reminder: Optional[Reminder],
    ) -> Reminder:
        if reminder is None:
            raise ReminderRepositoryError(
                ReminderRepositoryTypeError.REMINDER_NOT_FOUND
            )
        return reminder

    @staticmethod
    def user_owns_reminder(
        reminder_repository: ReminderRepository,
        user_uuid: Uuid,
        reminder_uuid: Uuid,
    ) -> None:
        reminder = ReminderRepositoryValidator.reminder_found(
            reminder_repository.find_by_id(reminder_uuid)
        )
        if reminder.user_uuid != user_uuid:
            raise ReminderRepositoryError(
                ReminderRepositoryTypeError.REMINDER_NOT_OWNED_BY_USER
            )
