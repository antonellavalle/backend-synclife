from pydantic import BaseModel


class PydanticVerifyAccountResponseDTO(BaseModel):
    session_token: str
