from pydantic import BaseModel


class PydanticRegisterResponseDTO(BaseModel):
    msg: str
