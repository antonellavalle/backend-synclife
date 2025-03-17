from pydantic import BaseModel


class PydanticDeleteAccountResponseDTO(BaseModel):
    msg: str
