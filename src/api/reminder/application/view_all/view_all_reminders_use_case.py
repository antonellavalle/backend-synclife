from typing import List

from src.api.reminder.application.view_all.view_all_reminders_dto import (
    ViewAllRemindersDTO,
)
from src.api.reminder.domain.entities.reminder import Reminder
from src.api.reminder.domain.repositories.reminder_repository import ReminderRepository
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects.uuid import Uuid


class ViewAllRemindersUseCase:
    def __init__(
        self,
        reminder_repository: ReminderRepository,
        session_repository: SessionRepository,
    ):
        self.__reminder_repository = reminder_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAllRemindersDTO) -> List[Reminder]:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        reminders = self.__reminder_repository.find_all_by_user_id(
            Uuid(user_request_uuid)
        )

        return reminders
