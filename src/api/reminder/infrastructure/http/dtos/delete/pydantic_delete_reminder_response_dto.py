from pydantic import BaseModel


class PydanticDeleteReminderResponseDTO(BaseModel):
    msg: str
