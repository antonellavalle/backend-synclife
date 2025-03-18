from fastapi import APIRouter, Header

from src.api.inventory.infrastructure.http.controllers.fastapi_inventory_controller import (  # noqa: E501
    FastAPIInventoryController,
)
from src.api.inventory.infrastructure.http.dtos import (
    PydanticCreateItemRequestDTO,
    PydanticCreateItemResponseDTO,
    PydanticDeleteItemRequestDTO,
    PydanticDeleteItemResponseDTO,
    PydanticUpdateItemRequestDTO,
    PydanticUpdateItemResponseDTO,
    PydanticViewAllInventoryItemsResponseDTO,
    PydanticViewItemRequestDTO,
    PydanticViewItemResponseDTO,
)

router: APIRouter = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/", response_model=PydanticCreateItemResponseDTO)
async def create_inventory_item(
    dto: PydanticCreateItemRequestDTO,
    session_token: str = Header(...),
) -> PydanticCreateItemResponseDTO:
    return await FastAPIInventoryController.create(dto, session_token)


@router.get("/{inventory_id}", response_model=PydanticViewItemResponseDTO)
async def view_inventory_item(
    dto: PydanticViewItemRequestDTO,
    session_token: str = Header(...),
) -> PydanticViewItemResponseDTO:
    return await FastAPIInventoryController.view(dto, session_token)


@router.get("/", response_model=PydanticViewAllInventoryItemsResponseDTO)
async def view_all_inventory_items(
    session_token: str = Header(...),
) -> PydanticViewAllInventoryItemsResponseDTO:
    return await FastAPIInventoryController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateItemResponseDTO)
async def update_inventory_item(
    dto: PydanticUpdateItemRequestDTO,
    session_token: str = Header(...),
) -> PydanticUpdateItemResponseDTO:
    return await FastAPIInventoryController.update(dto, session_token)


@router.delete("/{inventory_id}", response_model=PydanticDeleteItemResponseDTO)
async def delete_inventory_item(
    dto: PydanticDeleteItemRequestDTO,
    session_token: str = Header(...),
) -> PydanticDeleteItemResponseDTO:
    return await FastAPIInventoryController.delete(dto, session_token)
