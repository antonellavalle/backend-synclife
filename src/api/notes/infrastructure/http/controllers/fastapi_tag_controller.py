from src.api.notes.application.tag.create.create_tag_use_case import CreateTagUseCase
from src.api.notes.application.tag.delete.delete_tag_use_case import DeleteTagUseCase
from src.api.notes.application.tag.update.update_tag_use_case import UpdateTagUseCase
from src.api.notes.application.tag.view.view_tag_use_case import ViewTagUseCase
from src.api.notes.application.tag.view_all.view_all_tags_use_case import (
    ViewAllTagUseCase,
)
from src.api.notes.infrastructure.http.dtos.tag.create.pydantic_create_tag_request_dto import (  # noqa: E501 # noqa: E501
    PydanticCreateTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.create.pydantic_create_tag_response_dto import (  # noqa: E501
    PydanticCreateTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.delete.pydantic_delete_tag_request_dto import (  # noqa: E501
    PydanticDeleteTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.delete.pydantic_delete_tag_response_dto import (  # noqa: E501
    PydanticDeleteTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.update.pydantic_update_tag_request_dto import (  # noqa: E501
    PydanticUpdateTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.update.pydantic_update_tag_response_dto import (  # noqa: E501
    PydanticUpdateTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.view.pydantic_view_tag_request_dto import (  # noqa: E501
    PydanticViewTagRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.view.pydantic_view_tag_response_dto import (  # noqa: E501
    PydanticViewTagResponseDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.view_all.pydantic_view_all_tags_request_dto import (  # noqa: E501
    PydanticViewAllTagsRequestDTO,
)
from src.api.notes.infrastructure.http.dtos.tag.view_all.pydantic_view_all_tags_response_dto import (  # noqa: E501
    PydanticViewAllTagsResponseDTO,
    TagResponseType,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_tag_model import (
    SQLModelTagModel,
)
from src.api.notes.infrastructure.persistence.repositories.sqlmodel_tag_repository import (  # noqa: E501
    SQLModelTagRepository,
)
from src.api.shared.infrastructure.http.decorators.handle_exceptions import (
    handle_exceptions,
)
from src.api.shared.infrastructure.persistence.repositories.dragonfly_session_repository import (  # noqa: E501
    DragonflySessionRepository,
)


class FastAPITagController:
    @staticmethod
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateTagRequestDTO, session_token: str
    ) -> PydanticCreateTagResponseDTO:
        tag_repo = SQLModelTagRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = CreateTagUseCase(
            tag_repository=tag_repo, session_repository=session_repo
        )
        dto = request_dto.to_application(session_token=session_token)

        tag = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticCreateTagResponseDTO(
            tag=SQLModelTagModel.from_entity(entity=tag)
        )

    @staticmethod
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateTagRequestDTO, session_token: str
    ) -> PydanticUpdateTagResponseDTO:
        tag_repo = SQLModelTagRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = UpdateTagUseCase(
            tag_repository=tag_repo, session_repository=session_repo
        )
        dto = request_dto.to_application(session_token=session_token)

        tag = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticUpdateTagResponseDTO(
            tag=SQLModelTagModel.from_entity(entity=tag)
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteTagRequestDTO, session_token: str
    ) -> PydanticDeleteTagResponseDTO:
        tag_repo = SQLModelTagRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = DeleteTagUseCase(
            tag_repository=tag_repo, session_repository=session_repo
        )
        dto = request_dto.to_application(session_token=session_token)

        tag = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticDeleteTagResponseDTO(
            tag=SQLModelTagModel.from_entity(entity=tag)
        )

    @staticmethod
    @handle_exceptions
    async def view(tag_uuid: str, session_token: str) -> PydanticViewTagResponseDTO:
        tag_repo = SQLModelTagRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewTagUseCase(
            tag_repository=tag_repo, session_repository=session_repo
        )
        dto = PydanticViewTagRequestDTO(tag_uuid=tag_uuid).to_application(
            session_token=session_token
        )

        tag = use_case.execute(dto=dto)

        # TODO: optimizar response
        return PydanticViewTagResponseDTO(tag=SQLModelTagModel.from_entity(entity=tag))

    @staticmethod
    @handle_exceptions
    async def view_all(session_token: str) -> PydanticViewAllTagsResponseDTO:
        tag_repo = SQLModelTagRepository.get_repository()
        session_repo = DragonflySessionRepository.get_repository()

        use_case = ViewAllTagUseCase(
            tag_repository=tag_repo, session_repository=session_repo
        )
        dto = PydanticViewAllTagsRequestDTO().to_application(
            session_token=session_token
        )

        tags = use_case.execute(dto=dto)

        response_tags = [TagResponseType.from_entity(entity=tag) for tag in tags]

        # TODO: optimizar response
        return PydanticViewAllTagsResponseDTO(tags=response_tags)
