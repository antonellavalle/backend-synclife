from enum import Enum
from typing import Dict, cast

from src.api.notes.domain.errors.note.note_error import NoteError


class NoteRepositoryTypeError(Enum):
    DUPLICATED_TITLE = {"msg": "Ya existe una nota con ese titulo.", "code": 400}
    NOT_FOUND = {"msg": "No se encontro esta nota.", "code": 400}
    NOT_OWNED = {"msg": "Esta nota no pertenece al usuario.", "code": 400}
    OPERATION_FAILED = {
        "msg": "La operacion no pudo completarse. Intentalo nuevamente.",
        "code": 400,
    }


class NoteRepositoryError(NoteError):
    def __init__(self, error_type: NoteRepositoryTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
