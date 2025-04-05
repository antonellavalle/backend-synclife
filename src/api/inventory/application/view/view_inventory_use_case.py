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
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class ViewInventoryUseCase:
    def __init__(
        self,
        inventory_repository: InventoryRepository,
        user_repository: UserRepository,
        session_repository: SessionRepository,
    ):
        self.__inventory_repository = inventory_repository
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewInventoryDTO) -> Inventory:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            session_repository=self.__session_repository,
            session_token=dto.session_token,
        )

        user = UserRepositoryValidator.user_found(
            user=self.__user_repository.find_by_uuid(uuid=Uuid(uuid=user_request_uuid))
        )

        UserRepositoryValidator.user_is_verified(user=user)

        inventory_uuid = Uuid(uuid=dto.inventory_uuid)
        inventory = InventoryRepositoryValidator.inventory_found(
            inventory=self.__inventory_repository.find_by_uuid(uuid=inventory_uuid)
        )

        InventoryRepositoryValidator.user_owns_inventory(
            inventory_repository=self.__inventory_repository,
            user_uuid=Uuid(uuid=user_request_uuid),
            inventory_uuid=inventory_uuid,
        )

        return inventory
