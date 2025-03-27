from pydantic import BaseModel

from src.api.user.application.authentication.verify_account.verify_account_dto import (
    VerifyAccountDTO,
)


class PydanticVerifyAccountRequestDTO(BaseModel):
    @staticmethod
    def to_application(validate_token: str) -> VerifyAccountDTO:
        return VerifyAccountDTO(validate_token=validate_token)
