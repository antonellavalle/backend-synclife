from typing import Dict, List

from pydantic import BaseModel


class PydanticViewAllRemindersResponseDTO(BaseModel):
    items: List[Dict[str, str | object]]
