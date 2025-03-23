from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class PydanticRegisterResponseDTO(BaseModel):
    user: SQLModelUserModel
