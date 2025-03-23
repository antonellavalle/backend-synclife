from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.inventory.domain.entities.inventory import Inventory
from src.api.shared.domain.value_objects import Uuid


class InventoryRepository(ABC):
    @abstractmethod
    def find_all(self, include_deleted: bool = False) -> List[Inventory]:
        pass

    @abstractmethod
    def find_by_uuid(
        self, uuid: Uuid, include_deleted: bool = False
    ) -> Optional[Inventory]:
        pass

    @abstractmethod
    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Inventory]:
        pass

    @abstractmethod
    def save(self, inventory: Inventory) -> bool:
        pass

    @abstractmethod
    def delete(self, inventory: Inventory) -> Tuple[bool, Optional[Inventory]]:
        pass

    @abstractmethod
    def update(self, inventory: Inventory) -> Tuple[bool, Optional[Inventory]]:
        pass
