from typing import List

from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SQLModelNotesModel,
)


class PydanticViewAllNotesResponseDTO(BaseModel):
    notes: List[SQLModelNotesModel]
