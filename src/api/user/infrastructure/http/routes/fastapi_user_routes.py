from fastapi import APIRouter, Header

from src.api.user.infrastructure.http.controllers.fastapi_account_management_controller import (  # noqa: E501
    FastAPIAccountManagementController,
)
from src.api.user.infrastructure.http.controllers.fastapi_authentication_controller import (  # noqa: E501
    FastAPIAuthenticationController,
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
from src.api.user.infrastructure.http.dtos.account_management.view_account.pydantic_view_account_response_dto import (  # noqa: E501
    PydanticViewAccountResponseDTO,
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
from src.api.user.infrastructure.http.dtos.authentication.verify_account.pydantic_verify_account_response_dto import (  # noqa: E501
    PydanticVerifyAccountResponseDTO,
)

router: APIRouter = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/register",
    response_model=PydanticRegisterResponseDTO,
)
async def register(
    request_dto: PydanticRegisterRequestDTO,
) -> PydanticRegisterResponseDTO:
    return await FastAPIAuthenticationController.register(request_dto)


@router.patch("/{validate_token}", response_model=PydanticVerifyAccountResponseDTO)
async def verify_account(validate_token: str) -> PydanticVerifyAccountResponseDTO:
    return await FastAPIAuthenticationController.verify_account(validate_token)


@router.post(
    "/login",
    response_model=PydanticLoginResponseDTO,
)
async def login(request_dto: PydanticLoginRequestDTO) -> PydanticLoginResponseDTO:
    return await FastAPIAuthenticationController.login(request_dto)


@router.get(
    "/",
    response_model=PydanticViewAccountResponseDTO,
)
async def view_account(
    session_token: str = Header(...),
) -> PydanticViewAccountResponseDTO:
    return await FastAPIAccountManagementController.view_account(session_token)


@router.delete(
    "/",
    response_model=PydanticDeleteAccountResponseDTO,
)
async def delete_account(
    request_dto: PydanticDeleteAccountRequestDTO, session_token: str = Header(...)
) -> PydanticDeleteAccountResponseDTO:
    return await FastAPIAccountManagementController.delete_account(
        request_dto, session_token
    )


@router.post(
    "/request-change-password",
    response_model=PydanticRequestChangePasswordResponseDTO,
)
async def request_change_password(
    request_dto: PydanticRequestChangePasswordRequestDTO,
) -> PydanticRequestChangePasswordResponseDTO:
    return await FastAPIAccountManagementController.request_change_password(request_dto)


@router.patch(
    "/change-password/{validate_token}",
    response_model=PydanticChangePasswordResponseDTO,
)
async def change_password(
    request_dto: PydanticChangePasswordRequestDTO, validate_token: str
) -> PydanticChangePasswordResponseDTO:
    return await FastAPIAccountManagementController.change_password(
        request_dto, validate_token
    )


@router.put(
    "/",
    response_model=PydanticChangePersonalInformationResponseDTO,
)
async def change_personal_information(
    request_dto: PydanticChangePersonalInformationRequestDTO,
    session_token: str = Header(...),
) -> PydanticChangePersonalInformationResponseDTO:
    return await FastAPIAccountManagementController.change_personal_information(
        request_dto, session_token
    )


@router.post(
    "/request-account-recovery",
    response_model=PydanticRequestAccountRecoveryResponseDTO,
)
async def request_account_recovery(
    request_dto: PydanticRequestAccountRecoveryRequestDTO,
) -> PydanticRequestAccountRecoveryResponseDTO:
    return await FastAPIAccountManagementController.request_account_recovery(
        request_dto
    )


@router.patch(
    "/account-recovery/{validate_token}",
    response_model=PydanticAccountRecoveryResponseDTO,
)
async def account_recovery(
    request_dto: PydanticAccountRecoveryRequestDTO, validate_token: str
) -> PydanticAccountRecoveryResponseDTO:
    return await FastAPIAccountManagementController.account_recovery(
        request_dto, validate_token
    )
