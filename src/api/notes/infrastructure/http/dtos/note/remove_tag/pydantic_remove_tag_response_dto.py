from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_note_model import (
    SQLModelNoteModel,
)


class PydanticRemoveTagResponseDTO(BaseModel):
    note: SQLModelNoteModel
