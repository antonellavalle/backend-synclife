from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticRequestChangePasswordResponseDto(BaseModel):
    user: SqlModelUserModel
