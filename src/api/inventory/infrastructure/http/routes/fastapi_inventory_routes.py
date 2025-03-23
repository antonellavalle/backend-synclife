from fastapi import APIRouter, Header

from src.api.inventory.infrastructure.http.controllers.fastapi_inventory_controller import (  # noqa: E501
    FastAPIInventoryController,
)
from src.api.inventory.infrastructure.http.dtos.create.pydantic_create_inventory_request_dto import (  # noqa: E501
    PydanticCreateInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.create.pydantic_create_inventory_response_dto import (  # noqa: E501
    PydanticCreateInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.delete.pydantic_delete_inventory_request_dto import (  # noqa: E501
    PydanticDeleteInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.delete.pydantic_delete_inventory_response_dto import (  # noqa: E501
    PydanticDeleteInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.update.pydantic_update_inventory_request_dto import (  # noqa: E501
    PydanticUpdateInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.update.pydantic_update_inventory_response_dto import (  # noqa: E501
    PydanticUpdateInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.view.pydantic_view_inventory_response_dto import (  # noqa: E501
    PydanticViewInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.view_all.pydantic_view_all_inventory_response_dto import (  # noqa: E501
    PydanticViewAllInventoryResponseDTO,
)

router: APIRouter = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/", response_model=PydanticCreateInventoryResponseDTO)
async def create_inventory(
    dto: PydanticCreateInventoryRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateInventoryResponseDTO:
    return await FastAPIInventoryController.create(dto, session_token)


@router.get("/{inventory_uuid}", response_model=PydanticViewInventoryResponseDTO)
async def view_inventory(
    inventory_uuid: str,
    session_token: str = Header(...),
) -> PydanticViewInventoryResponseDTO:
    return await FastAPIInventoryController.view(inventory_uuid, session_token)


@router.get("/", response_model=PydanticViewAllInventoryResponseDTO)
async def view_all_inventory(
    session_token: str = Header(...),
) -> PydanticViewAllInventoryResponseDTO:
    return await FastAPIInventoryController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateInventoryResponseDTO)
async def update_inventory(
    dto: PydanticUpdateInventoryRequestDTO,
    session_token: str = Header(...),
) -> PydanticUpdateInventoryResponseDTO:
    return await FastAPIInventoryController.update(dto, session_token)


@router.delete("/", response_model=PydanticDeleteInventoryResponseDTO)
async def delete_inventory(
    dto: PydanticDeleteInventoryRequestDTO,
    session_token: str = Header(...),
) -> PydanticDeleteInventoryResponseDTO:
    return await FastAPIInventoryController.delete(dto, session_token)
