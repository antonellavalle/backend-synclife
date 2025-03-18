from fastapi import APIRouter, Header

from src.api.user.infrastructure.http.controllers import (
    FastApiAccountManagementController,
    FastApiAuthenticationController,
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
    PydanticLoginRequestDTO,
    PydanticLoginResponseDTO,
    PydanticRegisterRequestDTO,
    PydanticRegisterResponseDTO,
    PydanticRequestAccountRecoveryRequestDTO,
    PydanticRequestAccountRecoveryResponseDTO,
    PydanticRequestChangePasswordRequestDTO,
    PydanticRequestChangePasswordResponseDTO,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
    PydanticViewAccountRequestDTO,
    PydanticViewAccountResponseDTO,
)

router: APIRouter = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/register",
    response_model=PydanticRegisterResponseDTO,
)
async def register(
    request_dto: PydanticRegisterRequestDTO,
) -> PydanticRegisterResponseDTO:
    return await FastApiAuthenticationController.register(request_dto)


@router.get(
    "/{validate_token}",
    response_model=PydanticVerifyAccountResponseDTO,
)
async def verify_account(
    request_dto: PydanticVerifyAccountRequestDTO, validate_token: str
) -> PydanticVerifyAccountResponseDTO:
    return await FastApiAuthenticationController.verify_account(
        request_dto, validate_token
    )


@router.post(
    "/login",
    response_model=PydanticLoginResponseDTO,
)
async def login(request_dto: PydanticLoginRequestDTO) -> PydanticLoginResponseDTO:
    return await FastApiAuthenticationController.login(request_dto)


@router.get(
    "/",
    response_model=PydanticViewAccountResponseDTO,
)
async def view_account(
    request_dto: PydanticViewAccountRequestDTO, session_token: str = Header(...)
) -> PydanticViewAccountResponseDTO:
    return await FastApiAccountManagementController.view_account(
        request_dto, session_token
    )


@router.delete(
    "/",
    response_model=PydanticDeleteAccountResponseDTO,
)
async def delete_account(
    request_dto: PydanticDeleteAccountRequestDTO, session_token: str = Header(...)
) -> PydanticDeleteAccountResponseDTO:
    return await FastApiAccountManagementController.delete_account(
        request_dto, session_token
    )


@router.post(
    "/request-change-password",
    response_model=PydanticRequestChangePasswordResponseDTO,
)
async def request_change_password(
    request_dto: PydanticRequestChangePasswordRequestDTO,
) -> PydanticRequestChangePasswordResponseDTO:
    return await FastApiAccountManagementController.request_change_password(request_dto)


@router.patch(
    "/change-password/{validate_token}",
    response_model=PydanticChangePasswordResponseDTO,
)
async def change_password(
    request_dto: PydanticChangePasswordRequestDTO, validate_token: str
) -> PydanticChangePasswordResponseDTO:
    return await FastApiAccountManagementController.change_password(
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
    return await FastApiAccountManagementController.change_personal_information(
        request_dto, session_token
    )


@router.post(
    "/request-account-recovery",
    response_model=PydanticRequestAccountRecoveryResponseDTO,
)
async def request_account_recovery(
    request_dto: PydanticRequestAccountRecoveryRequestDTO,
) -> PydanticRequestAccountRecoveryResponseDTO:
    return await FastApiAccountManagementController.request_account_recovery(
        request_dto
    )


@router.patch(
    "/account-recovery/{validate_token}",
    response_model=PydanticAccountRecoveryResponseDTO,
)
async def account_recovery(
    request_dto: PydanticAccountRecoveryRequestDTO, validate_token: str
) -> PydanticAccountRecoveryResponseDTO:
    return await FastApiAccountManagementController.account_recovery(
        request_dto, validate_token
    )
