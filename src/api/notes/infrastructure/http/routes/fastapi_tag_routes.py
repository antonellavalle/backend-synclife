from fastapi import APIRouter, Header

from src.api.notes.infrastructure.http.controllers.fastapi_tag_controller import (  # noqa: E501
    FastAPITagController,
)
from src.api.notes.infrastructure.http.dtos.tag.create.pydantic_create_tag_request_dto import (  # noqa: E501
    PydanticCreateTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.create.pydantic_create_tag_response_dto import (  # noqa: E501
    PydanticCreateTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.delete.pydantic_delete_tag_request_dto import (  # noqa: E501
    PydanticDeleteTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.delete.pydantic_delete_tag_response_dto import (  # noqa: E501
    PydanticDeleteTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.update.pydantic_update_tag_request_dto import (  # noqa: E501
    PydanticUpdateTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.update.pydantic_update_tag_response_dto import (  # noqa: E501
    PydanticUpdateTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.view.pydantic_view_tag_response_dto import (  # noqa: E501
    PydanticViewTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.view_all.pydantic_view_all_tags_response_dto import (  # noqa: E501
    PydanticViewAllTagsResponseDTO,
)

router: APIRouter = APIRouter(prefix="/tag", tags=["Tag"])


@router.post("/", response_model=PydanticCreateTagResponseDTO)
async def create_tag(
    dto: PydanticCreateTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateTagResponseDTO:
    return await FastAPITagController.create(dto, session_token)


@router.get("/{tag_uuid}", response_model=PydanticViewTagResponseDTO)
async def view_tag(
    tag_uuid: str,
    session_token: str = Header(...),
) -> PydanticViewTagResponseDTO:
    return await FastAPITagController.view(tag_uuid, session_token)


@router.get("/", response_model=PydanticViewAllTagsResponseDTO)
async def view_all_tags(
    session_token: str = Header(...),
) -> PydanticViewAllTagsResponseDTO:
    return await FastAPITagController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateTagResponseDTO)
async def update_tag(
    dto: PydanticUpdateTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticUpdateTagResponseDTO:
    return await FastAPITagController.update(dto, session_token)


@router.delete("/", response_model=PydanticDeleteTagResponseDTO)
async def delete_tag(
    dto: PydanticDeleteTagRequestDTO,
    session_token: str = Header(...),
) -> PydanticDeleteTagResponseDTO:
    return await FastAPITagController.delete(dto, session_token)
