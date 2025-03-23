from pydantic import BaseModel, EmailStr

from src.api.user.application.account_management.modify_user.request_change_password.request_change_password_dto import (  # noqa: E501
    RequestChangePasswordDTO,
)


class PydanticRequestChangePasswordRequestDTO(BaseModel):
    email: EmailStr

    def to_application(self, url: str) -> RequestChangePasswordDTO:
        return RequestChangePasswordDTO(email=self.email, url=url)
