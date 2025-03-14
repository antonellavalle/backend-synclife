from src.api.reminder.application.update.update_reminder_dto import UpdateReminderDTO
from src.api.reminder.domain.entities import Reminder
from src.api.reminder.domain.errors import (
    ReminderRepositoryError,
    ReminderRepositoryTypeError,
)
from src.api.reminder.domain.repositories import ReminderRepository
from src.api.reminder.domain.validators.reminder_repository_validator import (
    ReminderRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class UpdateReminderUseCase:
    def __init__(
        self,
        reminder_repository: ReminderRepository,
        session_repository: SessionRepository,
    ):
        self.__reminder_repository = reminder_repository
        self.__session_repository = session_repository

    def execute(self, dto: UpdateReminderDTO) -> Reminder:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        reminder_uuid = Uuid(dto.reminder_uuid)
        reminder = ReminderRepositoryValidator.reminder_found(
            self.__reminder_repository.find_by_id(reminder_uuid)
        )

        ReminderRepositoryValidator.user_owns_reminder(
            reminder_repository=self.__reminder_repository,
            user_uuid=Uuid(user_request_uuid),
            reminder_uuid=reminder_uuid,
        )

        reminder.title = dto.title
        reminder.remind_date = dto.remind_date

        is_modified, reminder_modified = self.__reminder_repository.update(reminder)
        if not is_modified or reminder_modified is None:
            raise ReminderRepositoryError(ReminderRepositoryTypeError.OPERATION_FAILED)

        return reminder_modified
