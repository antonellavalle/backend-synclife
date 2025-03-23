from pydantic import BaseModel

from src.api.inventory.application.view.view_inventory_dto import ViewInventoryDTO


class PydanticViewInventoryRequestDTO(BaseModel):
    inventory_uuid: str

    def to_application(self, session_token: str) -> ViewInventoryDTO:
        return ViewInventoryDTO(
            inventory_uuid=self.inventory_uuid, session_token=session_token
        )
