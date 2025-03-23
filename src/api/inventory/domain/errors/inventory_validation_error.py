from enum import Enum
from typing import Dict, cast

from src.api.inventory.domain.errors.inventory_error import InventoryError


class InventoryValidationTypeError(Enum):
    INVALID_PRODUCT_NAME = {
        "msg": "El nombre del producto no puede estar vacio.",
        "code": 400,
    }
    INVALID_AMOUNT = {
        "msg": "La cantidad del producto debe ser mayor a 0.",
        "code": 400,
    }
    EXPIRED_ITEM = {
        "msg": "La fecha de expiracion del producto es invalida o ya expiro.",
        "code": 400,
    }


class InventoryValidationError(InventoryError):
    def __init__(self, error_type: InventoryValidationTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
