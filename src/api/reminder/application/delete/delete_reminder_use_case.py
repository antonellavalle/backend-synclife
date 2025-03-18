from src.api.reminder.application.delete.delete_reminder_dto import DeleteReminderDTO
from src.api.reminder.domain.errors.reminder_repository_error import (
    ReminderRepositoryError,
    ReminderRepositoryTypeError,
)
from src.api.reminder.domain.repositories.reminder_repository import ReminderRepository
from src.api.reminder.domain.validators.reminder_repository_validator import (
    ReminderRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class DeleteReminderUseCase:
    def __init__(
        self,
        reminder_repository: ReminderRepository,
        session_repository: SessionRepository,
    ):
        self.__reminder_repository = reminder_repository
        self.__session_repository = session_repository

    def execute(self, dto: DeleteReminderDTO) -> None:
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

        is_deleted, reminder_deleted = self.__reminder_repository.delete(reminder)
        if not is_deleted or reminder_deleted is None:
            raise ReminderRepositoryError(ReminderRepositoryTypeError.OPERATION_FAILED)
