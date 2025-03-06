from pydantic import BaseModel, EmailStr

from src.api.user.application.account_management.modify_user.request_change_password.request_change_password_dto import (  # noqa: E501
    RequestChangePasswordDto,
)


class PydanticRequestChangePasswordRequestDto(BaseModel):
    email: EmailStr

    def to_application(self, url: str) -> RequestChangePasswordDto:
        return RequestChangePasswordDto(email=self.email, url=url)
