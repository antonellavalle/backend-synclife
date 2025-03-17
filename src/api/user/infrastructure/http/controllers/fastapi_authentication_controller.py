import os

from dotenv import load_dotenv
from fastapi import APIRouter

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


class FastApiAuthenticationController:
    __router: APIRouter = APIRouter(prefix="/users", tags=["Users"])

    @classmethod
    def router(cls) -> APIRouter:
        return cls.__router

    @staticmethod
    @__router.post(
        "/register",
        name="Register",
        description="Register a new user by providing required details.",
        response_model=PydanticRegisterResponseDTO,
    )
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

        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users"

        app_dto = request_dto.to_application(url=url)
        use_case.execute(app_dto)

        return PydanticRegisterResponseDTO(
            msg="The confirmation email was sent correctly.",
        )

    @staticmethod
    @__router.get(
        "/{validate_token}",
        name="Verify Account",
        description="Verify a user's account using a token.",
        response_model=PydanticVerifyAccountResponseDTO,
    )
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
    @__router.post(
        "/login",
        name="Login",
        description="Authenticate a user with email and password.",
        response_model=PydanticLoginResponseDTO,
    )
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
