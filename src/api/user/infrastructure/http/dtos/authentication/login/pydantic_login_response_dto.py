from pydantic import BaseModel


class PydanticLoginResponseDTO(BaseModel):
    session_token: str
