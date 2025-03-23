from pydantic import BaseModel

from src.api.inventory.application.delete.delete_inventory_dto import DeleteInventoryDTO


class PydanticDeleteInventoryRequestDTO(BaseModel):
    inventory_uuid: str

    def to_application(self, session_token: str) -> DeleteInventoryDTO:
        return DeleteInventoryDTO(
            inventory_uuid=self.inventory_uuid, session_token=session_token
        )
