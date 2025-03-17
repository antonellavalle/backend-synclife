from pydantic import BaseModel


class PydanticRequestChangePasswordResponseDTO(BaseModel):
    msg: str
