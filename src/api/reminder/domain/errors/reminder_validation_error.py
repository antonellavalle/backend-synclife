from enum import Enum
from typing import Dict, cast

from src.api.reminder.domain.errors.reminder_error import ReminderError


class ReminderValidationTypeError(Enum):
    INVALID_TITLE = {
        "msg": "El nombre del recordatorio no puede ser nulo.",
        "code": 400,
    }
    INVALID_REMINDER_DATE = {
        "msg": "La fecha del recordatorio debe ser mayor a la fecha actual.",
        "code": 400,
    }


class ReminderValidationError(ReminderError):
    def __init__(self, error_type: ReminderValidationTypeError):
        super().__init__(error=cast(Dict[str, str | int], error_type.value))
