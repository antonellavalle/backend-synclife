from enum import Enum
from typing import Dict, cast

from src.api.inventory.domain.errors.inventory_error import InventoryError


class InventoryRepositoryTypeError(Enum):
    NOT_FOUND = {"msg": "No se encontro el producto", "code": 400}
    NOT_OWNED_BY_USER = {"msg": "Este inventario no pertenece al usuario", "code": 400}
    OPERATION_FAILED = {
        "msg": "La operación no pudo completarse. Inténtalo nuevamente.",
        "code": 400,
    }


class InventoryRepositoryError(InventoryError):
    def __init__(self, error_type: InventoryRepositoryTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
