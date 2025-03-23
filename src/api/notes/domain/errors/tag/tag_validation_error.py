from enum import Enum
from typing import Dict, cast

from src.api.notes.domain.errors.tag.tag_error import TagError


class TagValidationTypeError(Enum):
    INVALID_NAME = {"msg": "El nombre del tag no puede estar vacio.", "code": 400}
    NAME_MAX = {
        "msg": "El nombre del tag debe tener menos de 200 caracteres",
        "code": 400,
    }


class TagValidationError(TagError):
    def __init__(self, error_type: TagValidationTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
