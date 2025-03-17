from pydantic import BaseModel


class PydanticChangePasswordResponseDTO(BaseModel):
    msg: str
