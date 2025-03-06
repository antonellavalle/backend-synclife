from pydantic import BaseModel

from src.api.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDto,
)


class PydanticChangePasswordRequestDto(BaseModel):
    new_password: str

    def to_application(self, validate_token: str) -> ChangePasswordDto:
        return ChangePasswordDto(
            validate_token=validate_token, new_password=self.new_password
        )
