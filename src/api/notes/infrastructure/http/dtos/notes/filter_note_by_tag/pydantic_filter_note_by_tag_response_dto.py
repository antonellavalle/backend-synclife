from typing import List

from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SqlModelNotesModel,
)


class PydanticFilterNotesByTagResponseDTO(BaseModel):
    notes: List[SqlModelNotesModel]
