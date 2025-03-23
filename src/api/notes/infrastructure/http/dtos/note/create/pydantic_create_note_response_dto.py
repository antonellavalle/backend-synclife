from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_note_model import (
    SQLModelNoteModel,
)


class PydanticCreateNoteResponseDTO(BaseModel):
    note: SQLModelNoteModel
