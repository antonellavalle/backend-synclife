from pydantic import BaseModel

from src.api.inventory.application.view_all.view_all_inventory_dto import (
    ViewAllInventoryDTO,
)


class PydanticViewAllInventoryRequestDTO(BaseModel):
    def to_application(self, session_token: str) -> ViewAllInventoryDTO:
        return ViewAllInventoryDTO(
            session_token=session_token,
        )
