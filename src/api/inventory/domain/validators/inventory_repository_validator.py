from typing import Optional

from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.errors.inventory_repository_error import (
    InventoryRepositoryError,
    InventoryRepositoryTypeError,
)
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.shared.domain.value_objects import Uuid


class InventoryRepositoryValidator:
    @staticmethod
    def inventory_found(
        inventory: Optional[Inventory],
    ) -> Inventory:
        if inventory is None:
            raise InventoryRepositoryError(
                error_type=InventoryRepositoryTypeError.NOT_FOUND
            )
        return inventory

    @staticmethod
    def user_owns_inventory(
        inventory_repository: InventoryRepository,
        user_uuid: Uuid,
        inventory_uuid: Uuid,
    ) -> None:
        inventory = inventory_repository.find_by_uuid(uuid=inventory_uuid)
        if inventory is None or inventory.user_uuid != user_uuid:
            raise InventoryRepositoryError(
                error_type=InventoryRepositoryTypeError.NOT_OWNED_BY_USER
            )
