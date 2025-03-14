"""
Module that implements the authentication controller in the user infrastructure layer.

This controller defines the HTTP endpoints to manage authentication operations,
including:
  - User registration (POST /users/register)
  - Account verification (GET /users/verify-account/{validate_token})
  - User login (POST /users/login)

FastAPI is used along with decorators for centralized exception handling and integration
of the application use cases. Each endpoint converts the input DTO into the application
DTO, executes the corresponding use case, and transforms the domain entity into the
persistence model for the response.
"""

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
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)
from src.api.user.infrastructure.persistence.repositories import (
    DragonflyValidationTokenRepository,
    SQLModelUserRepository,
)


class FastApiAuthenticationController:
    """
    Authentication controller for the user infrastructure layer.

    This class defines the endpoints for:
      - Registering a user.
      - Verifying a user's account via a token.
      - Logging in a user.

    All methods are decorated with @handle_exceptions for uniform error handling.
    """

    __router: APIRouter = APIRouter(prefix="/users", tags=["Users"])

    @classmethod
    def router(cls) -> APIRouter:
        """
        Returns the router configured for the authentication endpoints.

        Returns:
            APIRouter: FastAPI router with the defined endpoints.
        """
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
        """
        Endpoint to register a new user.

        Performs the following operations:
          1. Retrieves the user repository, validation token repository, and email
             sender repository.
          2. Instantiates the RegisterUseCase and converts the received DTO into the
             application DTO.
          3. Loads the environment variable 'URL_BASE' and constructs the URL for
             account verification.
          4. Executes the use case and returns the response with the registered user
             (transformed into the persistence model).

        Args:
            request_dto (PydanticRegisterRequestDTO): DTO containing the registration
                                                      data.

        Returns:
            PydanticRegisterResponseDTO: Response DTO containing the registered user's
                                         data.
        """
        user_repository = SQLModelUserRepository.get_repository()
        user_validation_repository = DragonflyValidationTokenRepository.get_repository()
        smtp_email_sender_repository = MailHogSMTPEmailSenderRepository.get_repository()

        use_case = RegisterUseCase(
            user_repository, smtp_email_sender_repository, user_validation_repository
        )

        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users/verify-account"

        app_dto = request_dto.to_application(url=url)
        user = use_case.execute(app_dto)

        return PydanticRegisterResponseDTO(
            user=SQLModelUserModel.from_entity(user),
        )

    @staticmethod
    @__router.get(
        "/verify-account/{validate_token}",
        name="Verify Account",
        description="Verify a user's account using a token.",
        response_model=PydanticVerifyAccountResponseDTO,
    )
    @handle_exceptions
    async def verify_account(
        request_dto: PydanticVerifyAccountRequestDTO, validate_token: str
    ) -> PydanticVerifyAccountResponseDTO:
        """
        Endpoint to verify a user's account.

        Performs the following operations:
          1. Retrieves the repositories for users, validation tokens, and sessions.
          2. Instantiates the VerifyAccountUseCase and converts the received DTO into
             the application DTO.
          3. Executes the use case, obtaining the verified user and a session token.
          4. Returns the response with the user (transformed into the persistence model)
             and the session token.

        Args:
            request_dto (PydanticVerifyAccountRequestDTO): DTO containing the validation
                                                           token.
            validate_token (str): Validation token extracted from the URL.

        Returns:
            PydanticVerifyAccountResponseDTO: Response DTO containing the verified
                                              user's data and the session token.
        """
        user_repository = SQLModelUserRepository.get_repository()
        user_validation_repository = DragonflyValidationTokenRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = VerifyAccountUseCase(
            user_repository, user_validation_repository, session_repository
        )
        app_dto = request_dto.to_application(validate_token=validate_token)
        user, session_token = use_case.execute(app_dto)

        return PydanticVerifyAccountResponseDTO(
            user=SQLModelUserModel.from_entity(user), session_token=session_token
        )

    @staticmethod
    @__router.post(
        "/login",
        name="Login",
        description="Authenticate a user with email and password.",
        response_model=PydanticLoginResponseDTO,
    )
    @handle_exceptions
    async def login(request_dto: PydanticLoginRequestDTO) -> PydanticLoginResponseDTO:
        """
        Endpoint to log in a user.

        Performs the following operations:
          1. Retrieves the repositories for users and sessions.
          2. Instantiates the LoginUseCase and converts the received DTO into the
             application DTO.
          3. Executes the use case, obtaining the authenticated user and a session
             token.
          4. Returns the response with the user (transformed into the persistence model)
             and the session token.

        Args:
            request_dto (PydanticLoginRequestDTO): DTO containing the login credentials.

        Returns:
            PydanticLoginResponseDTO: Response DTO containing the authenticated user's
                                      data and the session token.
        """
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()
        use_case = LoginUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application()
        user, session_token = use_case.execute(app_dto)

        return PydanticLoginResponseDTO(
            user=SQLModelUserModel.from_entity(user),
            session_token=session_token,
        )
