import os

from dotenv import load_dotenv

from src.api.shared.infrastructure.http.decorators.handle_exceptions import (
    handle_exceptions,
)
from src.api.shared.infrastructure.persistence.repositories.dragonfly_session_repository import (  # noqa: E501
    DragonflySessionRepository,
)
from src.api.shared.infrastructure.persistence.repositories.mailhog_smtp_email_sender_repository import (  # noqa: E501
    MailHogSMTPEmailSenderRepository,
)
from src.api.user.application.account_management.account_recovery.account_recovery_use_case import (  # noqa: E501
    AccountRecoveryUseCase,
)
from src.api.user.application.account_management.delete_account.delete_account_use_case import (  # noqa: E501
    DeleteAccountUseCase,
)
from src.api.user.application.account_management.modify_user.change_password.change_password_use_case import (  # noqa: E501
    ChangePasswordUseCase,
)
from src.api.user.application.account_management.modify_user.change_personal_information.change_personal_information_use_case import (  # noqa: E501
    ChangePersonalInformationUseCase,
)
from src.api.user.application.account_management.modify_user.request_change_password.request_change_password_use_case import (  # noqa: E501
    RequestChangePasswordUseCase,
)
from src.api.user.application.account_management.request_account_recovery.request_account_recovery_use_case import (  # noqa: E501
    RequestAccountRecoveryUseCase,
)
from src.api.user.application.account_management.view_account.view_account_use_case import (  # noqa: E501
    ViewAccountUseCase,
)
from src.api.user.infrastructure.http.dtos.account_management.account_recovery.pydantic_account_recovery_request_dto import (  # noqa: E501
    PydanticAccountRecoveryRequestDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.account_recovery.pydantic_account_recovery_response_dto import (  # noqa: E501
    PydanticAccountRecoveryResponseDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.change_password.pydantic_change_password_request_dto import (  # noqa: E501
    PydanticChangePasswordRequestDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.change_password.pydantic_change_password_response_dto import (  # noqa: E501
    PydanticChangePasswordResponseDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.change_personal_information.pydantic_change_personal_information_request_dto import (  # noqa: E501
    PydanticChangePersonalInformationRequestDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.change_personal_information.pydantic_change_personal_information_response_dto import (  # noqa: E501
    PydanticChangePersonalInformationResponseDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.delete_account.pydantic_delete_account_request_dto import (  # noqa: E501
    PydanticDeleteAccountRequestDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.delete_account.pydantic_delete_account_response_dto import (  # noqa: E501
    PydanticDeleteAccountResponseDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.request_account_recovery.pydantic_request_account_recovery_request_dto import (  # noqa: E501
    PydanticRequestAccountRecoveryRequestDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.request_account_recovery.pydantic_request_account_recovery_response_dto import (  # noqa: E501
    PydanticRequestAccountRecoveryResponseDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.request_change_password.pydantic_request_change_password_request_dto import (  # noqa: E501
    PydanticRequestChangePasswordRequestDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.request_change_password.pydantic_request_change_password_response_dto import (  # noqa: E501
    PydanticRequestChangePasswordResponseDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.view_account.pydantic_view_account_request_dto import (  # noqa: E501
    PydanticViewAccountRequestDTO,
)
from src.api.user.infrastructure.http.dtos.account_management.view_account.pydantic_view_account_response_dto import (  # noqa: E501
    PydanticViewAccountResponseDTO,
)
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)
from src.api.user.infrastructure.persistence.repositories.dragonfly_validation_token_repository import (  # noqa: E501
    DragonflyValidationTokenRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SQLModelUserRepository,
)


class FastAPIAccountManagementController:
    @staticmethod
    @handle_exceptions
    async def view_account(session_token: str) -> PydanticViewAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = ViewAccountUseCase(
            user_repository=user_repository, session_repository=session_repository
        )
        app_dto = PydanticViewAccountRequestDTO.to_application(
            session_token=session_token
        )

        user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticViewAccountResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user)
        )

    @staticmethod
    @handle_exceptions
    async def delete_account(
        request_dto: PydanticDeleteAccountRequestDTO, session_token: str
    ) -> PydanticDeleteAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = DeleteAccountUseCase(
            user_repository=user_repository, session_repository=session_repository
        )
        app_dto = request_dto.to_application(session_token=session_token)

        deleted_user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticDeleteAccountResponseDTO(
            user=SQLModelUserModel.from_entity(entity=deleted_user),
        )

    @staticmethod
    @handle_exceptions
    async def request_change_password(
        request_dto: PydanticRequestChangePasswordRequestDTO,
    ) -> PydanticRequestChangePasswordResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        validation_token_repository = (
            DragonflyValidationTokenRepository.get_repository()
        )
        smtp_email_sender_repository = MailHogSMTPEmailSenderRepository.get_repository()

        use_case = RequestChangePasswordUseCase(
            user_repository=user_repository,
            validation_token_repository=validation_token_repository,
            smtp_email_sender_repository=smtp_email_sender_repository,
        )

        # TODO: hay que cambiar esto para que despues sea la url del front
        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users/change-password"

        app_dto = request_dto.to_application(url=url)

        user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticRequestChangePasswordResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user),
        )

    @staticmethod
    @handle_exceptions
    async def change_password(
        request_dto: PydanticChangePasswordRequestDTO, validate_token: str
    ) -> PydanticChangePasswordResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        validation_token_repository = (
            DragonflyValidationTokenRepository.get_repository()
        )

        use_case = ChangePasswordUseCase(
            user_repository=user_repository,
            validation_token_repository=validation_token_repository,
        )
        app_dto = request_dto.to_application(validate_token=validate_token)

        user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticChangePasswordResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user),
        )

    @staticmethod
    @handle_exceptions
    async def change_personal_information(
        request_dto: PydanticChangePersonalInformationRequestDTO,
        session_token: str,
    ) -> PydanticChangePersonalInformationResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = ChangePersonalInformationUseCase(
            user_repository=user_repository, session_repository=session_repository
        )

        app_dto = request_dto.to_application(session_token=session_token)
        user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticChangePersonalInformationResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user)
        )

    @staticmethod
    @handle_exceptions
    async def request_account_recovery(
        request_dto: PydanticRequestAccountRecoveryRequestDTO,
    ) -> PydanticRequestAccountRecoveryResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        validation_token_repository = (
            DragonflyValidationTokenRepository.get_repository()
        )
        smtp_email_sender_repository = MailHogSMTPEmailSenderRepository.get_repository()

        use_case = RequestAccountRecoveryUseCase(
            user_repository=user_repository,
            validation_token_repository=validation_token_repository,
            smtp_email_sender_repository=smtp_email_sender_repository,
        )

        # TODO: hay que cambiar esto para que despues sea la url del front
        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users/account-recovery"

        app_dto = request_dto.to_application(url=url)
        user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticRequestAccountRecoveryResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user)
        )

    @staticmethod
    @handle_exceptions
    async def account_recovery(
        request_dto: PydanticAccountRecoveryRequestDTO, validate_token: str
    ) -> PydanticAccountRecoveryResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        validation_token_repository = (
            DragonflyValidationTokenRepository.get_repository()
        )

        use_case = AccountRecoveryUseCase(
            user_repository=user_repository,
            validation_token_repository=validation_token_repository,
        )

        app_dto = request_dto.to_application(validate_token=validate_token)
        user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticAccountRecoveryResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user)
        )
