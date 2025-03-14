from fastapi import APIRouter, Header

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
from src.api.reminder.infrastructure.persistence.models import SQLModelReminderModel
from src.api.reminder.infrastructure.persistence.repositories import (
    SQLModelReminderRepository,
)
from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    DragonflySessionRepository,
)


class FastAPIReminderController:
    __router: APIRouter = APIRouter(prefix="/reminder", tags=["Reminder"])

    @classmethod
    def router(cls) -> APIRouter:
        return cls.__router

    @staticmethod
    @__router.post(
        "/",
        name="Create Reminder",
        description="",
        response_model=PydanticCreateReminderResponseDTO,
    )
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateReminderRequestDTO,
        session_token: str = Header(...),
    ) -> PydanticCreateReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = CreateReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = request_dto.to_application(session_token)
        reminder = use_case.execute(dto)

        return PydanticCreateReminderResponseDTO(
            item=SQLModelReminderModel.from_entity(reminder)
        )

    @staticmethod
    @__router.put(
        "/",
        name="Update Reminder",
        description="",
        response_model=PydanticUpdateReminderResponseDTO,
    )
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateReminderRequestDTO, session_token: str = Header(...)
    ) -> PydanticUpdateReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = UpdateReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = request_dto.to_application(session_token)
        updated_item = use_case.execute(dto)

        return PydanticUpdateReminderResponseDTO(
            item=SQLModelReminderModel.from_entity(updated_item)
        )

    @staticmethod
    @__router.delete(
        "/",
        name="Delete Reminder",
        description="",
        response_model=PydanticDeleteReminderResponseDTO,
    )
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteReminderRequestDTO, session_token: str = Header(...)
    ) -> PydanticDeleteReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = DeleteReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = request_dto.to_application(session_token)
        deleted_item = use_case.execute(dto)

        return PydanticDeleteReminderResponseDTO(
            item=SQLModelReminderModel.from_entity(deleted_item)
        )

    @staticmethod
    @__router.get(
        "/{reminder_uuid}",
        name="View Reminder",
        description="",
        response_model=PydanticViewReminderResponseDTO,
    )
    @handle_exceptions
    async def view(
        reminder_uuid: str, session_token: str = Header(...)
    ) -> PydanticViewReminderResponseDTO:
        reminder_repo = SQLModelReminderRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewReminderUseCase(
            reminder_repository=reminder_repo, session_repository=session_repo
        )

        dto = PydanticViewReminderRequestDTO(
            reminder_uuid=reminder_uuid
        ).to_application(session_token=session_token)
        reminder_item = use_case.execute(dto)

        return PydanticViewReminderResponseDTO(
            item=SQLModelReminderModel.from_entity(reminder_item)
        )

    @staticmethod
    @__router.get(
        "/",
        name="View all Reminders",
        description="",
        response_model=PydanticViewAllRemindersResponseDTO,
    )
    @handle_exceptions
    async def view_all(
        session_token: str = Header(...),
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
            model_inventory = SQLModelReminderModel.from_entity(reminder_item)
            response_reminders_items.append(model_inventory)

        return PydanticViewAllRemindersResponseDTO(items=response_reminders_items)
