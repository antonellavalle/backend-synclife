from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SQLModelInventoryModel,
)
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.shared.infrastructure.persistence.sqlmodel_connection import (
    get_session as get_db_connection,
)


class SQLModelInventoryRepository(InventoryRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SQLModelInventoryRepository":
        with get_db_connection() as db_connection:
            return SQLModelInventoryRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Inventory]:
        query = (
            select(SQLModelInventoryModel)
            if include_deleted
            else select(SQLModelInventoryModel).where(
                not_(SQLModelInventoryModel.is_deleted)
            )
        )
        items = self.db_connection.exec(query).all()
        return [item.to_entity() for item in items]

    def find_by_uuid(
        self, uuid: Uuid, include_deleted: bool = False
    ) -> Optional[Inventory]:
        query = (
            select(SQLModelInventoryModel).where(
                SQLModelInventoryModel.uuid == str(uuid)
            )
            if include_deleted
            else (
                select(SQLModelInventoryModel)
                .where(SQLModelInventoryModel.uuid == str(uuid))
                .where(not_(SQLModelInventoryModel.is_deleted))
            )
        )
        item = self.db_connection.exec(query).first()
        return item.to_entity() if item else None

    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Inventory]:
        query = select(SQLModelInventoryModel).where(
            SQLModelInventoryModel.user_uuid == str(user_uuid)
        )

        if not include_deleted:
            query = query.where(not_(SQLModelInventoryModel.is_deleted))

        items = self.db_connection.exec(query).all()
        return [item.to_entity() for item in items]

    def save(self, inventory: Inventory) -> bool:
        item_model = SQLModelInventoryModel.from_entity(inventory)
        self.db_connection.add(item_model)
        self.db_connection.commit()
        return True

    def update(self, inventory: Inventory) -> Tuple[bool, Optional[Inventory]]:
        existing_item = self.db_connection.exec(
            select(SQLModelInventoryModel)
            .where(SQLModelInventoryModel.uuid == str(inventory.uuid))
            .where(not_(SQLModelInventoryModel.is_deleted))
        ).first()

        if not existing_item:
            return (False, None)

        updates = {
            "product_name": inventory.product_name,
            "amount": inventory.amount,
            "expiration_date": inventory.expiration_date,
            "updated_at": datetime.now(),
        }
        for field, value in updates.items():
            if getattr(existing_item, field) != value:
                setattr(existing_item, field, value)

        self.db_connection.add(existing_item)
        self.db_connection.commit()
        self.db_connection.refresh(existing_item)

        result = (True, existing_item.to_entity())
        print(f"update() result: {result}")  # Imprime el resultado antes de devolverlo
        return result

    def delete(self, inventory: Inventory) -> Tuple[bool, Optional[Inventory]]:
        existing_item = self.db_connection.exec(
            select(SQLModelInventoryModel)
            .where(SQLModelInventoryModel.uuid == str(inventory.uuid))
            .where(not_(SQLModelInventoryModel.is_deleted))
        ).first()

        if not existing_item:
            return (False, None)

        existing_item.is_deleted = True
        existing_item.updated_at = datetime.now()
        self.db_connection.add(existing_item)
        self.db_connection.commit()
        self.db_connection.refresh(existing_item)

        return (True, existing_item.to_entity())
