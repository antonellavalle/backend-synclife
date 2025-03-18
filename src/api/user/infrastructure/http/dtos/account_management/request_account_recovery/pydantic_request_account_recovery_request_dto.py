from pydantic import BaseModel, EmailStr

from src.api.user.application.account_management.request_account_recovery import (
    RequestAccountRecoveryDTO,
)


class PydanticRequestAccountRecoveryRequestDTO(BaseModel):
    email: EmailStr

    def to_application(self, url: str) -> RequestAccountRecoveryDTO:
        return RequestAccountRecoveryDTO(email=self.email, url=url)
