from pydantic import BaseModel


class PydanticAccountRecoveryResponseDTO(BaseModel):
    msg: str
