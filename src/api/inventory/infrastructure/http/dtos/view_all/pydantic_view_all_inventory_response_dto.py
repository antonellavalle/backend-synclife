from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


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


class PydanticViewAllInventoryResponseDTO(BaseModel):
    inventory_items: List[InventoryResponseType]
