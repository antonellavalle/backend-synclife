from fastapi import APIRouter, Header

from src.api.reminder.infrastructure.http.controllers import (
    FastAPIReminderController,
)
from src.api.reminder.infrastructure.http.dtos import (
    PydanticCreateReminderRequestDTO,
    PydanticCreateReminderResponseDTO,
    PydanticDeleteReminderRequestDTO,
    PydanticDeleteReminderResponseDTO,
    PydanticUpdateReminderRequestDTO,
    PydanticUpdateReminderResponseDTO,
    PydanticViewAllRemindersResponseDTO,
    PydanticViewReminderResponseDTO,
)

router: APIRouter = APIRouter(prefix="/reminder", tags=["Reminder"])


@router.post(
    "/",
    response_model=PydanticCreateReminderResponseDTO,
)
async def create(
    request_dto: PydanticCreateReminderRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateReminderResponseDTO:
    return await FastAPIReminderController.create(request_dto, session_token)


@router.put(
    "/",
    response_model=PydanticUpdateReminderResponseDTO,
)
async def update(
    request_dto: PydanticUpdateReminderRequestDTO, session_token: str = Header(...)
) -> PydanticUpdateReminderResponseDTO:
    return await FastAPIReminderController.update(request_dto, session_token)


@router.delete(
    "/",
    response_model=PydanticDeleteReminderResponseDTO,
)
async def delete(
    request_dto: PydanticDeleteReminderRequestDTO, session_token: str = Header(...)
) -> PydanticDeleteReminderResponseDTO:
    return await FastAPIReminderController.delete(request_dto, session_token)


@router.get(
    "/{reminder_uuid}",
    response_model=PydanticViewReminderResponseDTO,
)
async def view(
    reminder_uuid: str, session_token: str = Header(...)
) -> PydanticViewReminderResponseDTO:
    return await FastAPIReminderController.view(reminder_uuid, session_token)


@router.get(
    "/",
    response_model=PydanticViewAllRemindersResponseDTO,
)
async def view_all(
    session_token: str = Header(...),
) -> PydanticViewAllRemindersResponseDTO:
    return await FastAPIReminderController.view_all(session_token)
