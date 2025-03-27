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
from src.api.user.application.authentication.login.login_use_case import LoginUseCase
from src.api.user.application.authentication.register.register_use_case import (
    RegisterUseCase,
)
from src.api.user.application.authentication.verify_account.verify_account_use_case import (  # noqa: E501
    VerifyAccountUseCase,
)
from src.api.user.infrastructure.http.dtos.authentication.login.pydantic_login_request_dto import (  # noqa: E501
    PydanticLoginRequestDTO,
)
from src.api.user.infrastructure.http.dtos.authentication.login.pydantic_login_response_dto import (  # noqa: E501
    PydanticLoginResponseDTO,
)
from src.api.user.infrastructure.http.dtos.authentication.register.pydantic_register_request_dto import (  # noqa: E501
    PydanticRegisterRequestDTO,
)
from src.api.user.infrastructure.http.dtos.authentication.register.pydantic_register_response_dto import (  # noqa: E501
    PydanticRegisterResponseDTO,
)
from src.api.user.infrastructure.http.dtos.authentication.verify_account.pydantic_verify_account_request_dto import (  # noqa: E501
    PydanticVerifyAccountRequestDTO,
)
from src.api.user.infrastructure.http.dtos.authentication.verify_account.pydantic_verify_account_response_dto import (  # noqa: E501
    PydanticVerifyAccountResponseDTO,
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


class FastAPIAuthenticationController:
    @staticmethod
    @handle_exceptions
    async def register(
        request_dto: PydanticRegisterRequestDTO,
    ) -> PydanticRegisterResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        user_validation_repository = DragonflyValidationTokenRepository.get_repository()
        smtp_email_sender_repository = MailHogSMTPEmailSenderRepository.get_repository()

        use_case = RegisterUseCase(
            user_repository=user_repository,
            smtp_email_sender_repository=smtp_email_sender_repository,
            validate_user_repository=user_validation_repository,
        )

        # TODO: hay que cambiar esto para que despues sea la url del front
        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users"

        app_dto = request_dto.to_application(url=url)
        user = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticRegisterResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user)
        )

    @staticmethod
    @handle_exceptions
    async def verify_account(validate_token: str) -> PydanticVerifyAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        user_validation_repository = DragonflyValidationTokenRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = VerifyAccountUseCase(
            user_repository=user_repository,
            validation_token_repository=user_validation_repository,
            session_repository=session_repository,
        )
        app_dto = PydanticVerifyAccountRequestDTO.to_application(
            validate_token=validate_token
        )
        user, session_token = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticVerifyAccountResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user), session_token=session_token
        )

    @staticmethod
    @handle_exceptions
    async def login(request_dto: PydanticLoginRequestDTO) -> PydanticLoginResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = LoginUseCase(
            user_repository=user_repository, session_repository=session_repository
        )

        app_dto = request_dto.to_application()
        user, session_token = use_case.execute(dto=app_dto)

        # TODO: optimizar response
        return PydanticLoginResponseDTO(
            user=SQLModelUserModel.from_entity(entity=user),
            session_token=session_token,
        )
