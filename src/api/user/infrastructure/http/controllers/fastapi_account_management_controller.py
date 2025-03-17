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
    PydanticChangePasswordRequestDTO,
    PydanticChangePasswordResponseDTO,
    PydanticChangePersonalInformationRequestDTO,
    PydanticChangePersonalInformationResponseDTO,
    PydanticDeleteAccountRequestDTO,
    PydanticDeleteAccountResponseDTO,
    PydanticRequestChangePasswordRequestDTO,
    PydanticRequestChangePasswordResponseDTO,
    PydanticViewAccountRequestDTO,
    PydanticViewAccountResponseDTO,
)
from src.api.user.infrastructure.persistence.repositories import (
    DragonflyValidationTokenRepository,
    SQLModelUserRepository,
)


class FastApiAccountManagementController:
    __router: APIRouter = APIRouter(prefix="/users", tags=["Users"])

    @classmethod
    def router(cls) -> APIRouter:
        return cls.__router

    @staticmethod
    @__router.get(
        "/",
        name="View Account",
        description="Retrieve user account details.",
        response_model=PydanticViewAccountResponseDTO,
    )
    @handle_exceptions
    async def view_account(
        request_dto: PydanticViewAccountRequestDTO, session_token: str = Header(...)
    ) -> PydanticViewAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = ViewAccountUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticViewAccountResponseDTO(
            email=str(user.email),
            birth_date=user.birth_date,
            full_name=user.full_name.get_full_name(),
            phone=str(user.phone),
        )

    @staticmethod
    @__router.delete(
        "/",
        name="Delete Account",
        description="Delete user account permanently.",
        response_model=PydanticDeleteAccountResponseDTO,
    )
    @handle_exceptions
    async def delete_account(
        request_dto: PydanticDeleteAccountRequestDTO, session_token: str = Header(...)
    ) -> PydanticDeleteAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = DeleteAccountUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        use_case.execute(app_dto)

        return PydanticDeleteAccountResponseDTO(
            msg="The user was successfully removed."
        )

    @staticmethod
    @__router.post(
        "/request-change-password",
        name="Request Change Password",
        description="Request a password reset link.",
        response_model=PydanticRequestChangePasswordResponseDTO,
    )
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

        load_dotenv()
        base_url = str(os.getenv("URL_BASE"))
        url = base_url + "/api/users/change-password"

        app_dto = request_dto.to_application(url=url)
        use_case.execute(app_dto)

        return PydanticRequestChangePasswordResponseDTO(
            msg="The confirmation email was sent correctly.",
        )

    @staticmethod
    @__router.patch(
        "/{validate_token}",
        description="Change user password using a validation token.",
        name="Change Password",
        response_model=PydanticChangePasswordResponseDTO,
    )
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
        use_case.execute(app_dto)

        return PydanticChangePasswordResponseDTO(
            msg="The password was successfully changed."
        )

    @staticmethod
    @__router.put(
        "/",
        description="Update user's personal information.",
        name="Change Personal Information",
        response_model=PydanticChangePersonalInformationResponseDTO,
    )
    @handle_exceptions
    async def change_personal_information(
        request_dto: PydanticChangePersonalInformationRequestDTO,
        session_token: str = Header(...),
    ) -> PydanticChangePersonalInformationResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = InMemorySessionRepository.get_repository()

        use_case = ChangePersonalInformationUseCase(user_repository, session_repository)

        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticChangePersonalInformationResponseDTO(
            email=str(user.email),
            birth_date=user.birth_date,
            full_name=user.full_name.get_full_name(),
            phone=str(user.phone),
        )
