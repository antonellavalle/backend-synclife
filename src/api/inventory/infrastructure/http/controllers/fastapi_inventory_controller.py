from src.api.inventory.application.create.create_inventory_use_case import (
    CreateInventoryUseCase,
)
from src.api.inventory.application.delete.delete_inventory_use_case import (
    DeleteInventoryUseCase,
)
from src.api.inventory.application.update.update_inventory_use_case import (
    UpdateInventoryUseCase,
)
from src.api.inventory.application.view.view_inventory_use_case import (
    ViewInventoryUseCase,
)
from src.api.inventory.application.view_all.view_all_inventory_use_case import (
    ViewAllInventoryUseCase,
)
from src.api.inventory.infrastructure.http.dtos.create.pydantic_create_inventory_request_dto import (  # noqa: E501
    PydanticCreateInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.create.pydantic_create_inventory_response_dto import (  # noqa: E501
    PydanticCreateInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.delete.pydantic_delete_inventory_request_dto import (  # noqa: E501
    PydanticDeleteInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.delete.pydantic_delete_inventory_response_dto import (  # noqa: E501
    PydanticDeleteInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.update.pydantic_update_inventory_request_dto import (  # noqa: E501
    PydanticUpdateInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.update.pydantic_update_inventory_response_dto import (  # noqa: E501
    PydanticUpdateInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.view.pydantic_view_inventory_request_dto import (  # noqa: E501
    PydanticViewInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.view.pydantic_view_inventory_response_dto import (  # noqa: E501
    PydanticViewInventoryResponseDTO,
)
from src.api.inventory.infrastructure.http.dtos.view_all.pydantic_view_all_inventory_request_dto import (  # noqa: E501
    PydanticViewAllInventoryRequestDTO,
)
from src.api.inventory.infrastructure.http.dtos.view_all.pydantic_view_all_inventory_response_dto import (  # noqa: E501
    InventoryResponseType,
    PydanticViewAllInventoryResponseDTO,
)
from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SQLModelInventoryModel,
)
from src.api.inventory.infrastructure.persistence.repositories.sqlmodel_inventory_repository import (  # noqa: E501
    SQLModelInventoryRepository,
)
from src.api.shared.infrastructure.http.decorators.handle_exceptions import (
    handle_exceptions,
)
from src.api.shared.infrastructure.persistence.repositories.dragonfly_session_repository import (  # noqa: E501
    DragonflySessionRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SQLModelUserRepository,
)


class FastAPIInventoryController:
    @staticmethod
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateInventoryRequestDTO, session_token: str
    ) -> PydanticCreateInventoryResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = CreateInventoryUseCase(
            inventory_repository=inventory_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        app_dto = request_dto.to_application(session_token=session_token)

        inventory = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticCreateInventoryResponseDTO(
            item=SQLModelInventoryModel.from_entity(entity=inventory)
        )

    @staticmethod
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateInventoryRequestDTO, session_token: str
    ) -> PydanticUpdateInventoryResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = UpdateInventoryUseCase(
            inventory_repository=inventory_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        app_dto = request_dto.to_application(session_token=session_token)

        inventory = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticUpdateInventoryResponseDTO(
            item=SQLModelInventoryModel.from_entity(entity=inventory)
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteInventoryRequestDTO, session_token: str
    ) -> PydanticDeleteInventoryResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_inventory = DragonflySessionRepository.get_repository()

        use_case = DeleteInventoryUseCase(
            inventory_repository=inventory_repo,
            user_repository=user_repo,
            session_repository=session_inventory,
        )
        dto = request_dto.to_application(session_token=session_token)

        inventory = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticDeleteInventoryResponseDTO(
            item=SQLModelInventoryModel.from_entity(entity=inventory)
        )

    @staticmethod
    @handle_exceptions
    async def view(
        inventory_uuid: str, session_token: str
    ) -> PydanticViewInventoryResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewInventoryUseCase(
            inventory_repository=inventory_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        app_dto = PydanticViewInventoryRequestDTO(
            inventory_uuid=inventory_uuid
        ).to_application(session_token=session_token)

        inventory = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticViewInventoryResponseDTO(
            item=SQLModelInventoryModel.from_entity(entity=inventory)
        )

    @staticmethod
    async def view_all(session_token: str) -> PydanticViewAllInventoryResponseDTO:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewAllInventoryUseCase(
            inventory_repository=inventory_repo,
            user_repository=user_repo,
            session_repository=session_repo,
        )
        app_dto = PydanticViewAllInventoryRequestDTO().to_application(
            session_token=session_token
        )

        inventory_items = use_case.execute(dto=app_dto)

        response_inventory_items = [
            InventoryResponseType.from_entity(entity=inventory)
            for inventory in inventory_items
        ]

        # TODO: optimizar response
        return PydanticViewAllInventoryResponseDTO(
            inventory_items=response_inventory_items
        )
