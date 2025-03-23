from src.api.inventory.application.update.update_inventory_dto import UpdateInventoryDTO
from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.errors.inventory_repository_error import (
    InventoryRepositoryError,
    InventoryRepositoryTypeError,
)
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


class UpdateInventoryUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        session_repository: SessionRepository,
    ) -> None:
        self.__inventory_repository = inventory_repository
        self.__session_repository = session_repository

    def execute(self, dto: UpdateInventoryDTO) -> Inventory:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        inventory_uuid = Uuid(uuid=dto.inventory_uuid)
        inventory = InventoryRepositoryValidator.inventory_found(
            inventory=self.__inventory_repository.find_by_uuid(uuid=inventory_uuid)
        )

        InventoryRepositoryValidator.user_owns_inventory(
            inventory_uuid=inventory_uuid,
            inventory_repository=self.__inventory_repository,
            user_uuid=Uuid(uuid=user_request_uuid),
        )

        inventory.product_name = dto.product_name
        inventory.amount = dto.amount
        inventory.expiration_date = dto.expiration_date

        is_updated, inventory_modified = self.__inventory_repository.update(
            inventory=inventory
        )

        if not is_updated or inventory_modified is None:
            raise InventoryRepositoryError(
                error_type=InventoryRepositoryTypeError.OPERATION_FAILED
            )

        return inventory_modified
