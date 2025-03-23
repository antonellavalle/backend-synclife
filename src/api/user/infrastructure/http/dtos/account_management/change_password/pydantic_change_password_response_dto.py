from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SQLModelUserModel,
)


class PydanticChangePasswordResponseDTO(BaseModel):
    user: SQLModelUserModel
