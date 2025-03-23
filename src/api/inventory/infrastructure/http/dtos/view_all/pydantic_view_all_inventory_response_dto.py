from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from src.api.inventory.domain.entities.inventory import Inventory


@dataclass
class InventoryResponseType:
    uuid: str
    user_uuid: str
    product_name: str
    amount: int
    expiration_date: date
    created_at: datetime
    updated_at: Optional[datetime]
    is_deleted: bool

    @staticmethod
    def from_entity(entity: Inventory) -> "InventoryResponseType":
        return InventoryResponseType(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            product_name=entity.product_name,
            amount=entity.amount,
            expiration_date=entity.expiration_date,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            is_deleted=entity.is_deleted,
        )


class PydanticViewAllInventoryResponseDTO(BaseModel):
    inventory_items: List[InventoryResponseType]
