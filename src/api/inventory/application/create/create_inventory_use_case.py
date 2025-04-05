from datetime import datetime

from src.api.inventory.application.create.create_inventory_dto import CreateInventoryDTO
from src.api.inventory.domain.entities.inventory import Inventory
from src.api.inventory.domain.errors.inventory_repository_error import (
    InventoryRepositoryError,
    InventoryRepositoryTypeError,
)
from src.api.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateInventoryUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        user_repository: UserRepository,
        session_repository: SessionRepository,
    ):
        self.__inventory_repository = inventory_repository
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: CreateInventoryDTO) -> Inventory:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        user = UserRepositoryValidator.user_found(
            user=self.__user_repository.find_by_uuid(uuid=Uuid(uuid=user_request_uuid))
        )

        UserRepositoryValidator.user_is_verified(user=user)

        inventory = Inventory(
            uuid=Uuid(),
            user_uuid=user.uuid,
            product_name=str(dto.product_name),
            amount=int(dto.amount),
            expiration_date=dto.expiration_date,
            created_at=datetime.now(),
            updated_at=None,
            is_deleted=False,
        )

        is_saved = self.__inventory_repository.save(inventory=inventory)

        if not is_saved:
            raise InventoryRepositoryError(
                InventoryRepositoryTypeError.OPERATION_FAILED
            )

        return inventory
