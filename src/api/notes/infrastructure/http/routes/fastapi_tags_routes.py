from fastapi import APIRouter, Header

from src.api.notes.infrastructure.http.controllers.tags.fastapi_tags_controller import (  # noqa: E501
    FastApiTagsController,
)
from src.api.notes.infrastructure.http.dtos.tags import (
    PydanticCreateTagRequestDTO,
    PydanticCreateTagResponseDTO,
    PydanticDeleteTagRequestDTO,
    PydanticDeleteTagResponseDTO,
    PydanticUpdateTagsRequestDTO,
    PydanticUpdateTagsResponseDTO,
    PydanticViewAllTagsResponseDTO,
    PydanticViewTagsRequestDTO,
    PydanticViewTagsResponseDTO,
)

router: APIRouter = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/", response_model=PydanticCreateTagResponseDTO)
async def create_tag(
    dto: PydanticCreateTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateTagResponseDTO:
    return await FastApiTagsController.create(dto, session_token)


@router.get("/{tag_id}", response_model=PydanticViewTagsResponseDTO)
async def view_tag(
    dto: PydanticViewTagsRequestDTO,
    session_token: str = Header(...),
) -> PydanticViewTagsResponseDTO:
    return await FastApiTagsController.view(dto, session_token)


@router.get("/", response_model=PydanticViewAllTagsResponseDTO)
async def view_all_tags(
    session_token: str = Header(...),
) -> PydanticViewAllTagsResponseDTO:
    return await FastApiTagsController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateTagsResponseDTO)
async def update_tags(
    dto: PydanticUpdateTagsRequestDTO,
    session_token: str = Header(...),
) -> PydanticUpdateTagsResponseDTO:
    return await FastApiTagsController.update(dto, session_token)


@router.delete("/{tag_id}", response_model=PydanticDeleteTagResponseDTO)
async def delete_tag(
    dto: PydanticDeleteTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticDeleteTagResponseDTO:
    return await FastApiTagsController.delete(dto, session_token)
