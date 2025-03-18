from enum import Enum
from typing import Dict, cast

from src.api.reminder.domain.errors.reminder_error import ReminderError


class ReminderRepositoryTypeError(Enum):
    NOT_FOUND = {"msg": "El recordatorio no fue encontrado.", "code": 400}
    NOT_OWNED_BY_USER = {
        "msg": "Este recordatorio no pertenece al usuario.",
        "code": 400,
    }
    OPERATION_FAILED = {"msg": "The operation failed.", "code": 400}


class ReminderRepositoryError(ReminderError):
    def __init__(self, error_type: ReminderRepositoryTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
