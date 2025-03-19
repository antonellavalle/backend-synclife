from pydantic import BaseModel

from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SQLModelInventoryModel,
)


class PydanticUpdateInventoryResponseDTO(BaseModel):
    item: SQLModelInventoryModel
