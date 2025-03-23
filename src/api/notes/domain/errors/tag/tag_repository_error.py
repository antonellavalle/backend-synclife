from enum import Enum
from typing import Dict, cast

from src.api.notes.domain.errors.tag.tag_error import TagError


class TagRepositoryTypeError(Enum):
    DUPLICATED_NAME = {"msg": "El nombre del tag ya existe", "code": 400}
    NOT_FOUND = {"msg": "No se encontro este tag", "code": 400}
    NOT_OWNED = {"msg": "Este tag no pertence al usuario", "code": 400}
    OPERATION_FAILED = {
        "msg": "La operacion no pudo completarse. Intentalo nuevamente",
        "code": 400,
    }


class TagRepositoryError(TagError):
    def __init__(self, error_type: TagRepositoryTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
