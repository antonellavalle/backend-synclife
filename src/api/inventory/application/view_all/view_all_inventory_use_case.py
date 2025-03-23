from typing import List

from src.api.inventory.application.view_all.view_all_inventory_dto import (
    ViewAllInventoryDTO,
)
from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects import Uuid


class ViewAllInventoryUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        session_repository: SessionRepository,
    ):
        self.__inventory_repository = inventory_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAllInventoryDTO) -> List[Inventory]:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        inventory_items = self.__inventory_repository.find_all_by_user_uuid(
            user_uuid=Uuid(uuid=user_request_uuid)
        )

        return inventory_items
