import os

from dotenv import load_dotenv

from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
    MailHogSMTPEmailSenderRepository,
)
from src.api.user.application import (
    ChangePasswordUseCase,
    ChangePersonalInformationUseCase,
    DeleteAccountUseCase,
    ViewAccountUseCase,
)
from src.api.user.application.account_management.modify_user.request_change_password import (  # noqa: E501
    RequestChangePasswordUseCase,
)
from src.api.user.infrastructure.http.dtos import (
    PydanticChangePasswordRequestDto,
    PydanticChangePasswordResponseDto,
    PydanticChangePersonalInformationRequestDto,
    PydanticChangePersonalInformationResponseDto,
    PydanticDeleteAccountRequestDto,
    PydanticDeleteAccountResponseDto,
    PydanticRequestChangePasswordRequestDto,
    PydanticRequestChangePasswordResponseDto,
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
)
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)
from src.api.user.infrastructure.persistence.repositories.dragonfly_validation_token_repository import (  # noqa: E501
    DragonflyValidationTokenRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)


class FastApiAccountManagementController:
    @staticmethod
    @handle_exceptions
    async def view_account(
        request_dto: PydanticViewAccountRequestDto, session_token: str
    ) -> PydanticViewAccountResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = ViewAccountUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticViewAccountResponseDto(user=SqlModelUserModel.from_entity(user))

    @staticmethod
    @handle_exceptions
    async def delete_account(
        request_dto: PydanticDeleteAccountRequestDto, session_token: str
    ) -> PydanticDeleteAccountResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = DeleteAccountUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticDeleteAccountResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )

    @staticmethod
    @handle_exceptions
    async def request_change_password(
        request_dto: PydanticRequestChangePasswordRequestDto,
    ) -> PydanticRequestChangePasswordResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        validation_token_repository = (
            DragonflyValidationTokenRepository.get_repository()
        )
        smtp_email_sender_repository = MailHogSMTPEmailSenderRepository.get_repository()

        use_case = RequestChangePasswordUseCase(
            user_repository=user_repository,
            validation_token_repository=validation_token_repository,
            smtp_email_sender_repository=smtp_email_sender_repository,
        )

        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users/change-password"

        app_dto = request_dto.to_application(url=url)
        user = use_case.execute(app_dto)

        return PydanticRequestChangePasswordResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )

    @staticmethod
    @handle_exceptions
    async def change_password(
        request_dto: PydanticChangePasswordRequestDto, validate_token: str
    ) -> PydanticChangePasswordResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        validation_token_repository = (
            DragonflyValidationTokenRepository.get_repository()
        )

        use_case = ChangePasswordUseCase(
            user_repository=user_repository,
            validation_token_repository=validation_token_repository,
        )
        app_dto = request_dto.to_application(validate_token=validate_token)
        user = use_case.execute(app_dto)

        return PydanticChangePasswordResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )

    @staticmethod
    @handle_exceptions
    async def change_personal_information(
        request_dto: PydanticChangePersonalInformationRequestDto, session_token: str
    ) -> PydanticChangePersonalInformationResponseDto:
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = ChangePersonalInformationUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticChangePersonalInformationResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )
