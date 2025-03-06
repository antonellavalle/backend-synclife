from fastapi import APIRouter, Header

from src.api.user.infrastructure.http.controllers import (
    FastApiAccountManagementController,
    FastApiAuthenticationController,
)
from src.api.user.infrastructure.http.dtos import (
    PydanticChangePasswordRequestDto,
    PydanticChangePasswordResponseDto,
    PydanticChangePersonalInformationRequestDto,
    PydanticChangePersonalInformationResponseDto,
    PydanticDeleteAccountRequestDto,
    PydanticDeleteAccountResponseDto,
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
    PydanticRequestChangePasswordRequestDto,
    PydanticRequestChangePasswordResponseDto,
    PydanticVerifyAccountRequestDTO,
    PydanticVerifyAccountResponseDTO,
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
)

router: APIRouter = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=PydanticRegisterResponseDto)
async def register_user(
    dto: PydanticRegisterRequestDto,
) -> PydanticRegisterResponseDto:
    return await FastApiAuthenticationController.register(dto)


@router.get(
    "/verify-account/{validate_token}",
    response_model=PydanticVerifyAccountResponseDTO,
)
async def verify_account(
    validate_token: str,
) -> PydanticVerifyAccountResponseDTO:
    return await FastApiAuthenticationController.validate_account(
        PydanticVerifyAccountRequestDTO(validate_token=validate_token)
    )


@router.post("/login", response_model=PydanticLoginResponseDto)
async def login_user(dto: PydanticLoginRequestDto) -> PydanticLoginResponseDto:
    return await FastApiAuthenticationController.login(dto)


@router.get("/", response_model=PydanticViewAccountResponseDto)
async def view_account_user(
    dto: PydanticViewAccountRequestDto,
    session_token: str = Header(...),
) -> PydanticViewAccountResponseDto:
    return await FastApiAccountManagementController.view_account(dto, session_token)


@router.post(
    "/request-change-password", response_model=PydanticRequestChangePasswordResponseDto
)
async def request_change_password(
    dto: PydanticRequestChangePasswordRequestDto,
) -> PydanticRequestChangePasswordResponseDto:
    return await FastApiAccountManagementController.request_change_password(dto)


@router.get(
    "/change-password/{validate_token}",
    response_model=PydanticChangePasswordResponseDto,
)
async def change_password(
    validate_token: str, dto: PydanticChangePasswordRequestDto
) -> PydanticChangePasswordResponseDto:
    return await FastApiAccountManagementController.change_password(dto, validate_token)


@router.put("/", response_model=PydanticChangePersonalInformationResponseDto)
async def change_user_personal_info(
    dto: PydanticChangePersonalInformationRequestDto,
    session_token: str = Header(...),
) -> PydanticChangePersonalInformationResponseDto:
    return await FastApiAccountManagementController.change_personal_information(
        dto, session_token
    )


@router.delete("/", response_model=PydanticDeleteAccountResponseDto)
async def delete_account_user(
    dto: PydanticDeleteAccountRequestDto,
    session_token: str = Header(...),
) -> PydanticDeleteAccountResponseDto:
    return await FastApiAccountManagementController.delete_account(dto, session_token)
