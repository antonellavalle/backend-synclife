from fastapi import APIRouter, Header

from src.api.reminder.infrastructure.http.controllers.fastapi_reminder_controller import (  # noqa: E501
    FastAPIReminderController,
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
from src.api.reminder.infrastructure.http.dtos.view.pydantic_view_reminder_response_dto import (  # noqa: E501
    PydanticViewReminderResponseDTO,
)
from src.api.reminder.infrastructure.http.dtos.view_all.pydantic_view_all_reminders_response_dto import (  # noqa: E501
    PydanticViewAllRemindersResponseDTO,
)

router: APIRouter = APIRouter(prefix="/reminder", tags=["Reminder"])


@router.post(
    "/",
    response_model=PydanticCreateReminderResponseDTO,
)
async def create_reminder(
    request_dto: PydanticCreateReminderRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateReminderResponseDTO:
    return await FastAPIReminderController.create(request_dto, session_token)


@router.put(
    "/",
    response_model=PydanticUpdateReminderResponseDTO,
)
async def update_reminder(
    request_dto: PydanticUpdateReminderRequestDTO, session_token: str = Header(...)
) -> PydanticUpdateReminderResponseDTO:
    return await FastAPIReminderController.update(request_dto, session_token)


@router.delete(
    "/",
    response_model=PydanticDeleteReminderResponseDTO,
)
async def delete_reminder(
    request_dto: PydanticDeleteReminderRequestDTO, session_token: str = Header(...)
) -> PydanticDeleteReminderResponseDTO:
    return await FastAPIReminderController.delete(request_dto, session_token)


@router.get(
    "/{reminder_uuid}",
    response_model=PydanticViewReminderResponseDTO,
)
async def view_reminder(
    reminder_uuid: str, session_token: str = Header(...)
) -> PydanticViewReminderResponseDTO:
    return await FastAPIReminderController.view(reminder_uuid, session_token)


@router.get(
    "/",
    response_model=PydanticViewAllRemindersResponseDTO,
)
async def view_all_reminders(
    session_token: str = Header(...),
) -> PydanticViewAllRemindersResponseDTO:
    return await FastAPIReminderController.view_all(session_token)
