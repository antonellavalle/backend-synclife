from src.api.inventory.application.create_item import CreateItemUseCase
from src.api.inventory.application.delete_item import DeleteItemUseCase
from src.api.inventory.application.update_item import UpdateItemUseCase
from src.api.inventory.application.view_all_items import ViewAllInventoryItemsUseCase
from src.api.inventory.application.view_all_items.view_all_item_dto import (
    ViewAllInventoryItemsDTO,
)
from src.api.inventory.application.view_item import ViewItemUseCase
from src.api.inventory.infrastructure.http.dtos import (
    PydanticCreateItemRequestDTO,
    PydanticCreateItemResponseDTO,
    PydanticDeleteItemRequestDTO,
    PydanticDeleteItemResponseDTO,
    PydanticUpdateItemRequestDTO,
    PydanticUpdateItemResponseDTO,
    PydanticViewAllInventoryItemsResponseDTO,
    PydanticViewItemRequestDTO,
    PydanticViewItemResponseDTO,
)
from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SQLModelInventoryModel,
)
from src.api.inventory.infrastructure.persistence.repositories import (
    SQLModelInventoryRepository,
)
from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SQLModelUserRepository,
)


class FastAPIInventoryController:
    @staticmethod
    @handle_exceptions
    async def create(
        item_data: PydanticCreateItemRequestDTO, session_token: str
    ) -> PydanticCreateItemResponseDTO:
        invenory_repo = SQLModelInventoryRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = CreateItemUseCase(invenory_repo, user_repo, session_repo)
        dto = item_data.to_application(session_token)
        item = use_case.execute(dto)

        return PydanticCreateItemResponseDTO(
            item=SQLModelInventoryModel.from_entity(item)
        )

    @staticmethod
    @handle_exceptions
    async def update(
        item_data: PydanticUpdateItemRequestDTO, session_token: str
    ) -> PydanticUpdateItemResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = UpdateItemUseCase(inventory_repo, session_repo)
        dto = item_data.to_application(session_token)
        updated_item = use_case.execute(dto)

        return PydanticUpdateItemResponseDTO(
            item=SQLModelInventoryModel.from_entity(updated_item)
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteItemRequestDTO, session_token: str
    ) -> PydanticDeleteItemResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_inventory = InMemorySessionRepository.get_repository()

        use_case = DeleteItemUseCase(inventory_repo, session_inventory)
        dto = request_dto.to_application(session_token)
        deleted_item = use_case.execute(dto)

        return PydanticDeleteItemResponseDTO(
            item=SQLModelInventoryModel.from_entity(deleted_item)
        )

    @staticmethod
    @handle_exceptions
    async def view(
        request_dto: PydanticViewItemRequestDTO, session_token: str
    ) -> PydanticViewItemResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewItemUseCase(inventory_repo, session_repo)
        dto = request_dto.to_application(session_token)
        item = use_case.execute(dto)

        return PydanticViewItemResponseDTO(
            item=SQLModelInventoryModel.from_entity(item)
        )

    @staticmethod
    async def view_all(session_token: str) -> PydanticViewAllInventoryItemsResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewAllInventoryItemsUseCase(inventory_repo, session_repo)
        dto = ViewAllInventoryItemsDTO(session_token=session_token)
        inventory_items = use_case.execute(dto)

        response_inventory_items = []
        for inventory_item in inventory_items:
            model_inventory = SQLModelInventoryModel.from_entity(inventory_item)
            response_inventory_items.append(model_inventory)

        return PydanticViewAllInventoryItemsResponseDTO(
            inventory_items=response_inventory_items
        )
