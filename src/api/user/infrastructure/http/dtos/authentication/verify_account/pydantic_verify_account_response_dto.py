from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class PydanticVerifyAccountResponseDTO(BaseModel):
    user: SQLModelUserModel
    session_token: str
