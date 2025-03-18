import os

from dotenv import load_dotenv

from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    DragonflySessionRepository,
    MailHogSMTPEmailSenderRepository,
)
from src.api.user.application import (
    AccountRecoveryUseCase,
    ChangePasswordUseCase,
    ChangePersonalInformationUseCase,
    DeleteAccountUseCase,
    RequestAccountRecoveryUseCase,
    RequestChangePasswordUseCase,
    ViewAccountUseCase,
)
from src.api.user.infrastructure.http.dtos import (
    PydanticAccountRecoveryRequestDTO,
    PydanticAccountRecoveryResponseDTO,
    PydanticChangePasswordRequestDTO,
    PydanticChangePasswordResponseDTO,
    PydanticChangePersonalInformationRequestDTO,
    PydanticChangePersonalInformationResponseDTO,
    PydanticDeleteAccountRequestDTO,
    PydanticDeleteAccountResponseDTO,
    PydanticRequestAccountRecoveryRequestDTO,
    PydanticRequestAccountRecoveryResponseDTO,
    PydanticRequestChangePasswordRequestDTO,
    PydanticRequestChangePasswordResponseDTO,
    PydanticViewAccountRequestDTO,
    PydanticViewAccountResponseDTO,
)
from src.api.user.infrastructure.persistence.repositories import (
    DragonflyValidationTokenRepository,
    SQLModelUserRepository,
)


class FastAPIAccountManagementController:
    @staticmethod
    @handle_exceptions
    async def view_account(
        request_dto: PydanticViewAccountRequestDTO, session_token: str
    ) -> PydanticViewAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

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
    @handle_exceptions
    async def delete_account(
        request_dto: PydanticDeleteAccountRequestDTO, session_token: str
    ) -> PydanticDeleteAccountResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = DeleteAccountUseCase(user_repository, session_repository)
        app_dto = request_dto.to_application(session_token)
        use_case.execute(app_dto)

        return PydanticDeleteAccountResponseDTO(
            msg="The user was successfully removed."
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
        use_case.execute(app_dto)

        return PydanticRequestChangePasswordResponseDTO(
            msg="The confirmation email was sent correctly.",
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
        use_case.execute(app_dto)

        return PydanticChangePasswordResponseDTO(
            msg="The password was successfully changed."
        )

    @staticmethod
    @handle_exceptions
    async def change_personal_information(
        request_dto: PydanticChangePersonalInformationRequestDTO,
        session_token: str,
    ) -> PydanticChangePersonalInformationResponseDTO:
        user_repository = SQLModelUserRepository.get_repository()
        session_repository = DragonflySessionRepository.get_repository()

        use_case = ChangePersonalInformationUseCase(user_repository, session_repository)

        app_dto = request_dto.to_application(session_token)
        user = use_case.execute(app_dto)

        return PydanticChangePersonalInformationResponseDTO(
            email=str(user.email),
            birth_date=user.birth_date,
            full_name=user.full_name.get_full_name(),
            phone=str(user.phone),
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
        use_case.execute(app_dto)

        return PydanticRequestAccountRecoveryResponseDTO(
            msg="The confirmation email was sent correctly."
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
        use_case.execute(app_dto)

        return PydanticAccountRecoveryResponseDTO(
            msg="The account was successfully recovered."
        )
