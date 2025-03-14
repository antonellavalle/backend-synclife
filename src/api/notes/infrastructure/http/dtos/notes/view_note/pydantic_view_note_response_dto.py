from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SQLModelNotesModel,
)


class PydanticViewNotesResponseDTO(BaseModel):
    note: SQLModelNotesModel
