import os

from dotenv import load_dotenv

from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    DragonflySessionRepository,
    MailHogSMTPEmailSenderRepository,
)
from src.api.user.application.authentication import (
    LoginUseCase,
    RegisterUseCase,
    VerifyAccountUseCase,
)
from src.api.user.infrastructure.http.dtos import (
    PydanticLoginRequestDTO,
    PydanticLoginResponseDTO,
    PydanticRegisterRequestDTO,
    PydanticRegisterResponseDTO,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
)
from src.api.user.infrastructure.persistence.repositories import (
    DragonflyValidationTokenRepository,
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
            user_repository, smtp_email_sender_repository, user_validation_repository
        )

        # TODO: hay que cambiar esto para que despues sea la url del front
        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users"

        app_dto = request_dto.to_application(url=url)
        use_case.execute(app_dto)

        return PydanticRegisterResponseDTO(
            msg="The confirmation email was sent correctly.",
        )

    @staticmethod
    @handle_exceptions
    async def verify_account(
        request_dto: PydanticVerifyAccountRequestDTO, validate_token: str
    ) -> PydanticVerifyAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        user_validation_repository = DragonflyValidationTokenRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = VerifyAccountUseCase(
            user_repository, user_validation_repository, session_repository
        )
        app_dto = request_dto.to_application(validate_token=validate_token)
        session_token = use_case.execute(app_dto)

        return PydanticVerifyAccountResponseDTO(session_token=session_token)

    @staticmethod
    @handle_exceptions
    async def login(request_dto: PydanticLoginRequestDTO) -> PydanticLoginResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = LoginUseCase(user_repository, session_repository)

        app_dto = request_dto.to_application()
        session_token = use_case.execute(app_dto)

        return PydanticLoginResponseDTO(
            session_token=session_token,
        )
