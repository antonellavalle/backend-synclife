from pydantic import BaseModel

from src.api.user.application.account_management.account_recovery.account_recovery_dto import (  # noqa: E501
    AccountRecoveryDTO,
)


class PydanticAccountRecoveryRequestDTO(BaseModel):
    def to_application(self, validate_token: str) -> AccountRecoveryDTO:
        return AccountRecoveryDTO(validate_token=validate_token)
