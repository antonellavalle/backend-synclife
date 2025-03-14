from datetime import date

from pydantic import BaseModel

from src.api.inventory.application.update_item.update_item_dto import UpdateItemDTO


class PydanticUpdateItemRequestDTO(BaseModel):
    inventory_id: str
    product_name: str
    amount: int
    expiration_date: date

    def to_application(self, session_token: str) -> UpdateItemDTO:
        return UpdateItemDTO(
            inventory_id=self.inventory_id,
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
            session_token=session_token,
        )
