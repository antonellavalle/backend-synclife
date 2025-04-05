from src.api.reminder.application.create.create_reminder_use_case import (
    CreateReminderUseCase,
)
from src.api.reminder.application.delete.delete_reminder_use_case import (
    DeleteReminderUseCase,
)
from src.api.reminder.application.update.update_reminder_use_case import (
    UpdateReminderUseCase,
)
from src.api.reminder.application.view.view_reminder_use_case import ViewReminderUseCase
from src.api.reminder.application.view_all.view_all_reminders_use_case import (
    ViewAllRemindersUseCase,
)
from src.api.reminder.infrastructure.http.dtos.create.pydantic_create_reminder_request_dto import (  # noqa: E501
    PydanticCreateReminderRequestDTO,
)
from src.api.reminder.infrastructure.http.dtos.create.pydantic_create_reminder_response_dto import (  # noqa: E501
    PydanticCreateReminderResponseDTO,
)
from src.api.reminder.infrastructure.http.dtos.delete.pydantic_delete_reminder_request_dto import (  # noqa: E501
    PydanticDeleteReminderRequestDTO,
)
from src.api.reminder.infrastructure.http.dtos.delete.pydantic_delete_reminder_response_dto import (  # noqa: E501
    PydanticDeleteReminderResponseDTO,
)
from src.api.reminder.infrastructure.http.dtos.update.pydantic_update_reminder_request_dto import (  # noqa: E501
    PydanticUpdateReminderRequestDTO,
)
from src.api.reminder.infrastructure.http.dtos.update.pydantic_update_reminder_response_dto import (  # noqa: E501
    PydanticUpdateReminderResponseDTO,
)
from src.api.reminder.infrastructure.http.dtos.view.pydantic_view_reminder_request_dto import (  # noqa: E501
    PydanticViewReminderRequestDTO,
)
from src.api.reminder.infrastructure.http.dtos.view.pydantic_view_reminder_response_dto import (  # noqa: E501
    PydanticViewReminderResponseDTO,
)
from src.api.reminder.infrastructure.http.dtos.view_all.pydantic_view_all_reminders_request_dto import (  # noqa: E501
    PydanticViewAllRemindersRequestDTO,
)
from src.api.reminder.infrastructure.http.dtos.view_all.pydantic_view_all_reminders_response_dto import (  # noqa: E501
    PydanticViewAllRemindersResponseDTO,
    ReminderResponseType,
)
from src.api.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (
    SQLModelReminderModel,
)
from src.api.reminder.infrastructure.persistence.repositories.sqlmodel_reminder_repository import (  # noqa: E501
    SQLModelReminderRepository,
)
from src.api.shared.infrastructure.http.decorators.handle_exceptions import (
    handle_exceptions,
)
from src.api.shared.infrastructure.persistence.repositories.dragonfly_session_repository import (  # noqa: E501
    DragonflySessionRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SQLModelUserRepository,
)


class FastAPIReminderController:
    @staticmethod
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateReminderRequestDTO,
        session_token: str,
    ) -> PydanticCreateReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = CreateReminderUseCase(
            reminder_repository=reminder_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = request_dto.to_application(session_token=session_token)

        reminder = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticCreateReminderResponseDTO(
            reminder=SQLModelReminderModel.from_entity(entity=reminder)
        )

    @staticmethod
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateReminderRequestDTO, session_token: str
    ) -> PydanticUpdateReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = UpdateReminderUseCase(
            reminder_repository=reminder_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = request_dto.to_application(session_token=session_token)

        reminder = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticUpdateReminderResponseDTO(
            reminder=SQLModelReminderModel.from_entity(entity=reminder)
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteReminderRequestDTO, session_token: str
    ) -> PydanticDeleteReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = DeleteReminderUseCase(
            reminder_repository=reminder_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = request_dto.to_application(session_token=session_token)

        reminder = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticDeleteReminderResponseDTO(
            reminder=SQLModelReminderModel.from_entity(entity=reminder)
        )

    @staticmethod
    @handle_exceptions
    async def view(
        reminder_uuid: str, session_token: str
    ) -> PydanticViewReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewReminderUseCase(
            reminder_repository=reminder_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = PydanticViewReminderRequestDTO(
            reminder_uuid=reminder_uuid
        ).to_application(session_token=session_token)

        reminder = use_case.execute(dto)

        # TODO: optimizar response
        return PydanticViewReminderResponseDTO(
            reminder=SQLModelReminderModel.from_entity(entity=reminder)
        )

    @staticmethod
    @handle_exceptions
    async def view_all(
        session_token: str,
    ) -> PydanticViewAllRemindersResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewAllRemindersUseCase(
            reminder_repository=reminder_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        dto = PydanticViewAllRemindersRequestDTO().to_application(
            session_token=session_token
        )

        reminders = use_case.execute(dto)

        response_reminders_items = [
            ReminderResponseType.from_entity(entity=reminder) for reminder in reminders
        ]

        # TODO: optimizar response
        return PydanticViewAllRemindersResponseDTO(items=response_reminders_items)
