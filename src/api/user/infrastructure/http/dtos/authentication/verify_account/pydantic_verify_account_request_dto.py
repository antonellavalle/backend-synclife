from pydantic import BaseModel

from src.api.user.application.authentication.verify_account.verify_account_dto import (
    VerifyAccountDTO,
)


class PydanticVerifyAccountRequestDTO(BaseModel):
    def to_application(self, validate_token: str) -> VerifyAccountDTO:
        return VerifyAccountDTO(validate_token=validate_token)
