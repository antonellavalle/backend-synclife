from src.api.notes.application.tag.create_tag import CreateTagUseCase
from src.api.notes.application.tag.delete_tag import DeleteTagUseCase
from src.api.notes.application.tag.update_tag import UpdateTagUseCase
from src.api.notes.application.tag.view_all_tags import ViewAllTagsUseCase
from src.api.notes.application.tag.view_all_tags.view_all_tags_dto import ViewAllTagsDTO
from src.api.notes.application.tag.view_tag import ViewTagUseCase
from src.api.notes.infrastructure.http.dtos.tags import (
    PydanticCreateTagRequestDTO,
    PydanticCreateTagResponseDTO,
    PydanticDeleteTagRequestDTO,
    PydanticDeleteTagResponseDTO,
    PydanticUpdateTagsRequestDTO,
    PydanticUpdateTagsResponseDTO,
    PydanticViewAllTagsResponseDTO,
    PydanticViewTagsRequestDTO,
    PydanticViewTagsResponseDTO,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SQLModelTagsModel,
)
from src.api.notes.infrastructure.persistence.repositories.sqlmodel_tags_repository import (  # noqa: E501
    SQLModelTagsRepository,
)
from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SQLModelUserRepository,
)


class FastAPITagsController:
    @staticmethod
    @handle_exceptions
    async def create(
        request_dto: PydanticCreateTagRequestDTO, session_token: str
    ) -> PydanticCreateTagResponseDTO:
        tag_repo = SQLModelTagsRepository.get_repository()
        user_repo = SQLModelUserRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = CreateTagUseCase(tag_repo, user_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticCreateTagResponseDTO(tag=SQLModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def update(
        request_dto: PydanticUpdateTagsRequestDTO, session_token: str
    ) -> PydanticUpdateTagsResponseDTO:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = UpdateTagUseCase(tag_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticUpdateTagsResponseDTO(tag=SQLModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteTagRequestDTO, session_token: str
    ) -> PydanticDeleteTagResponseDTO:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = DeleteTagUseCase(tag_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticDeleteTagResponseDTO(tag=SQLModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def view(
        request_dto: PydanticViewTagsRequestDTO, session_token: str
    ) -> PydanticViewTagsResponseDTO:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewTagUseCase(tag_repo, session_repo)
        dto = request_dto.to_application(session_token)
        tag = use_case.execute(dto)

        return PydanticViewTagsResponseDTO(tag=SQLModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def view_all(session_token: str) -> PydanticViewAllTagsResponseDTO:
        tag_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewAllTagsUseCase(tag_repo, session_repo)

        dto = ViewAllTagsDTO(session_token=session_token)
        tags = use_case.execute(dto)

        response_tags = []
        for tag in tags:
            model_tag = SQLModelTagsModel.from_entity(tag)
            response_tags.append(model_tag)

        return PydanticViewAllTagsResponseDTO(tags=response_tags)
