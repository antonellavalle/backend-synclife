from datetime import date

from pydantic import BaseModel

from src.api.inventory.application.update.update_inventory_dto import UpdateInventoryDTO


class PydanticUpdateInventoryRequestDTO(BaseModel):
    inventory_id: str
    product_name: str
    amount: int
    expiration_date: date

    def to_application(self, session_token: str) -> UpdateInventoryDTO:
        return UpdateInventoryDTO(
            inventory_uuid=self.inventory_id,
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
            session_token=session_token,
        )
