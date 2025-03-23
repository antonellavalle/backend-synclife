from datetime import date

from pydantic import BaseModel

from src.api.inventory.application.create.create_inventory_dto import CreateInventoryDTO


class PydanticCreateInventoryRequestDTO(BaseModel):
    product_name: str
    amount: int
    expiration_date: date

    def to_application(self, session_token: str) -> CreateInventoryDTO:
        return CreateInventoryDTO(
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
            session_token=session_token,
        )
