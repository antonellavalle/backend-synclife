from src.api.reminder.application import (
    CreateReminderUseCase,
    DeleteReminderUseCase,
    UpdateReminderUseCase,
    ViewAllRemindersUseCase,
    ViewReminderUseCase,
)
from src.api.reminder.infrastructure.http.dtos import (
    PydanticCreateReminderRequestDTO,
    PydanticCreateReminderResponseDTO,
    PydanticDeleteReminderRequestDTO,
    PydanticDeleteReminderResponseDTO,
    PydanticUpdateReminderRequestDTO,
    PydanticUpdateReminderResponseDTO,
    PydanticViewAllRemindersRequestDTO,
    PydanticViewAllRemindersResponseDTO,
    PydanticViewReminderRequestDTO,
    PydanticViewReminderResponseDTO,
)
from src.api.reminder.infrastructure.persistence.repositories import (
    SQLModelReminderRepository,
)
from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    DragonflySessionRepository,
)


class FastAPIReminderController:
    @staticmethod
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateReminderRequestDTO,
        session_token: str,
    ) -> PydanticCreateReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = CreateReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = request_dto.to_application(session_token)
        reminder = use_case.execute(dto)

        return PydanticCreateReminderResponseDTO(
            uuid=str(reminder.uuid),
            title=reminder.title,
            remind_date=reminder.remind_date,
        )

    @staticmethod
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateReminderRequestDTO, session_token: str
    ) -> PydanticUpdateReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = UpdateReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = request_dto.to_application(session_token)
        reminder = use_case.execute(dto)

        return PydanticUpdateReminderResponseDTO(
            uuid=str(reminder.uuid),
            title=reminder.title,
            remind_date=reminder.remind_date,
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteReminderRequestDTO, session_token: str
    ) -> PydanticDeleteReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = DeleteReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = request_dto.to_application(session_token)
        use_case.execute(dto)

        return PydanticDeleteReminderResponseDTO(
            msg="The reminder was successfully deleted."
        )

    @staticmethod
    @handle_exceptions
    async def view(
        reminder_uuid: str, session_token: str
    ) -> PydanticViewReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = PydanticViewReminderRequestDTO(
            reminder_uuid=reminder_uuid
        ).to_application(session_token=session_token)
        reminder = use_case.execute(dto)

        return PydanticViewReminderResponseDTO(
            uuid=str(reminder.uuid),
            title=reminder.title,
            remind_date=reminder.remind_date,
        )

    @staticmethod
    @handle_exceptions
    async def view_all(
        session_token: str,
    ) -> PydanticViewAllRemindersResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewAllRemindersUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = PydanticViewAllRemindersRequestDTO().to_application(
            session_token=session_token
        )
        reminder_items = use_case.execute(dto)

        response_reminders_items = []
        for reminder_item in reminder_items:
            reminder = {
                "uuid": str(reminder_item.uuid),
                "title": reminder_item.title,
                "remind_date": reminder_item.remind_date,
            }
            response_reminders_items.append(reminder)

        return PydanticViewAllRemindersResponseDTO(items=response_reminders_items)
