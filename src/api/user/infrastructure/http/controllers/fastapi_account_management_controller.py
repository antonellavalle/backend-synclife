"""
Module that implements the account management controller in the user infrastructure
layer.

This controller uses FastAPI to define HTTP endpoints that expose the functionalities
for managing user accounts (viewing, deletion, password change, and personal information
modification). Centralized exception handling decorators are applied, and application
use cases are integrated.
"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Header

from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
    MailHogSMTPEmailSenderRepository,
)
from src.api.user.application import (
    ChangePasswordUseCase,
    ChangePersonalInformationUseCase,
    DeleteAccountUseCase,
    RequestChangePasswordUseCase,
    ViewAccountUseCase,
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
from src.api.user.infrastructure.persistence.repositories import (
    DragonflyValidationTokenRepository,
    SqlModelUserRepository,
)


class FastApiAccountManagementController:
    """
    Account management controller for the user infrastructure layer.

    This class defines HTTP endpoints for managing the user account, integrating the
    application use cases. It exposes methods to:
      - View the account.
      - Delete the account.
      - Request a password change.
      - Change the password.
      - Modify personal information.

    All methods are decorated with @handle_exceptions for uniform error handling.
    """

    __router: APIRouter = APIRouter(prefix="/users", tags=["Users"])

    @classmethod
    def router(cls) -> APIRouter:
        """
        Returns the router configured for account management endpoints.

        Returns:
            APIRouter: An instance of the router with the defined endpoints.
        """
        return cls.__router

    @staticmethod
    @__router.get(
        "/",
        name="View Account",
        description="Retrieve user account details.",
        response_model=PydanticViewAccountResponseDto,
    )
    @handle_exceptions
    async def view_account(
        request_dto: PydanticViewAccountRequestDto, session_token: str = Header(...)
    ) -> PydanticViewAccountResponseDto:
        """
        Endpoint to view a user's account.

        Performs the following operations:
          1. Obtains the user repository and the session repository.
          2. Instantiates the ViewAccountUseCase and converts the received DTO to the
             application DTO.
          3. Executes the use case to obtain the user and transforms it to the
             persistence model.

        Args:
            request_dto (PydanticViewAccountRequestDto): DTO containing the request
                                                         data.
            session_token (str): Session token extracted from the request header.

        Returns:
            PydanticViewAccountResponseDto: Response DTO containing the user account
                                            data.
        """
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = ViewAccountUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticViewAccountResponseDto(user=SqlModelUserModel.from_entity(user))

    @staticmethod
    @__router.delete(
        "/",
        name="Delete Account",
        description="Delete user account permanently.",
        response_model=PydanticDeleteAccountResponseDto,
    )
    @handle_exceptions
    async def delete_account(
        request_dto: PydanticDeleteAccountRequestDto, session_token: str = Header(...)
    ) -> PydanticDeleteAccountResponseDto:
        """
        Endpoint to delete a user's account.

        Performs the following operations:
          1. Obtains the user and session repositories.
          2. Instantiates the DeleteAccountUseCase and converts the received DTO to the
             application DTO.
          3. Executes the use case to delete the account and transforms the deleted user
             to the persistence model.

        Args:
            request_dto (PydanticDeleteAccountRequestDto): DTO containing the data to
                                                           delete the account.
            session_token (str): Session token extracted from the request header.

        Returns:
            PydanticDeleteAccountResponseDto: Response DTO containing the data of the
                                              deleted user.
        """
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = DeleteAccountUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticDeleteAccountResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )

    @staticmethod
    @__router.post(
        "/request-change-password",
        name="Request Change Password",
        description="Request a password reset link.",
        response_model=PydanticRequestChangePasswordResponseDto,
    )
    @handle_exceptions
    async def request_change_password(
        request_dto: PydanticRequestChangePasswordRequestDto,
    ) -> PydanticRequestChangePasswordResponseDto:
        """
        Endpoint to request a password change.

        Performs the following operations:
          1. Obtains the user, validation token, and email sender repositories.
          2. Instantiates the RequestChangePasswordUseCase.
          3. Loads the environment variable URL_BASE and constructs the URL for password
             change.
          4. Converts the received DTO to the application DTO, executes the use case,
             and transforms the resulting user to the persistence model.

        Args:
            request_dto (PydanticRequestChangePasswordRequestDto): DTO containing the
                                                                   data to request a
                                                                   password change.

        Returns:
            PydanticRequestChangePasswordResponseDto: Response DTO containing the user's
                                                      data.
        """
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
    @__router.patch(
        "/{validate_token}",
        description="Change user password using a validation token.",
        name="Change Password",
        response_model=PydanticChangePasswordResponseDto,
    )
    @handle_exceptions
    async def change_password(
        request_dto: PydanticChangePasswordRequestDto, validate_token: str
    ) -> PydanticChangePasswordResponseDto:
        """
        Endpoint to change the user's password.

        Performs the following operations:
          1. Obtains the user and validation token repositories.
          2. Instantiates the ChangePasswordUseCase.
          3. Converts the received DTO to the application DTO, executes the use case,
             and transforms the resulting user to the persistence model.

        Args:
            request_dto (PydanticChangePasswordRequestDto): DTO containing the new
                                                            password.
            validate_token (str): Validation token extracted from the URL.

        Returns:
            PydanticChangePasswordResponseDto: Response DTO containing the updated
                                               user's data.
        """
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
    @__router.put(
        "/",
        description="Update user's personal information.",
        name="Change Personal Information",
        response_model=PydanticChangePersonalInformationResponseDto,
    )
    @handle_exceptions
    async def change_personal_information(
        request_dto: PydanticChangePersonalInformationRequestDto,
        session_token: str = Header(...),
    ) -> PydanticChangePersonalInformationResponseDto:
        """
        Endpoint to modify the user's personal information.

        Performs the following operations:
          1. Obtains the user and session repositories.
          2. Instantiates the ChangePersonalInformationUseCase.
          3. Converts the received DTO to the application DTO, executes the use case,
             and transforms the resulting user to the persistence model.

        Args:
            request_dto (PydanticChangePersonalInformationRequestDto): DTO containing
                                                                       the new personal
                                                                       data.
            session_token (str): Session token extracted from the request header.

        Returns:
            PydanticChangePersonalInformationResponseDto: Response DTO containing the
                                                          updated user's data.
        """
        user_repository = SqlModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = ChangePersonalInformationUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticChangePersonalInformationResponseDto(
            user=SqlModelUserModel.from_entity(user)
        )
