from typing import List

from pydantic import BaseModel

from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)


class PydanticViewAllInventoryItemsResponseDTO(BaseModel):
    inventory_items: List[SqlModelInventoryModel]
