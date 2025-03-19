from src.api.inventory.application.view.view_inventory_dto import ViewInventoryDTO
from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.inventory.domain.validators.inventory_repository_validator import (
    InventoryRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class ViewInventoryUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        session_repository: SessionRepository,
    ):
        self.__inventory_repository = inventory_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewInventoryDTO) -> Inventory:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        inventory_uuid = Uuid(dto.inventory_uuid)
        inventory = InventoryRepositoryValidator.inventory_found(
            self.__inventory_repository.find_by_id(inventory_uuid)
        )

        InventoryRepositoryValidator.user_owns_inventory(
            repository=self.__inventory_repository,
            user_id=Uuid(user_request_uuid),
            inventory_id=inventory_uuid,
        )

        return inventory
