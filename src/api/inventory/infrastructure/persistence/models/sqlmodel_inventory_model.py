from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.api.inventory.domain.entities.inventory import Inventory
from src.api.shared.domain.value_objects import Uuid
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class SQLModelInventoryModel(SQLModel, table=True):
    __tablename__ = "inventory"

    uuid: str = Field(primary_key=True)
    user_uuid: str = Field(foreign_key="user.uuid")
    product_name: str
    amount: int
    expiration_date: date
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SQLModelUserModel" = Relationship(back_populates="inventory_items")

    @classmethod
    def from_entity(cls, entity: "Inventory") -> "SQLModelInventoryModel":
        return cls(
            uuid=str(entity.uuid),
            user_uuid=str(entity.user_uuid),
            product_name=entity.product_name,
            amount=entity.amount,
            expiration_date=entity.expiration_date,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> "Inventory":
        return Inventory(
            uuid=Uuid(uuid=self.uuid),
            user_uuid=Uuid(uuid=self.user_uuid),
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
