from pydantic import BaseModel

from src.api.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDTO,
)


class PydanticViewAccountRequestDTO(BaseModel):
    @staticmethod
    def to_application(session_token: str) -> ViewAccountDTO:
        return ViewAccountDTO(session_token=session_token)
