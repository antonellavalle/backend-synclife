from typing import Any, Awaitable, Callable, TypeVar

from fastapi import HTTPException

from src.api.inventory.domain.errors.inventory_error import InventoryError
from src.api.notes.domain.errors.note.note_error import NoteError
from src.api.notes.domain.errors.tag.tag_error import TagError
from src.api.reminder.domain.errors.reminder_error import ReminderError
from src.api.shared.domain.errors.shared_error import SharedError
from src.api.user.domain.errors.user_error import UserError

T = TypeVar("T")


def handle_exceptions(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
    async def wrapper(*args: Any, **kwargs: Any) -> T:
        try:
            return await func(*args, **kwargs)
        except (
            SharedError,
            UserError,
            NoteError,
            InventoryError,
            TagError,
            ReminderError,
        ) as error:
            detail = str(error)
            code = int(error.code)
            raise HTTPException(status_code=code, detail=detail)
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Error interno del servidor: {error}"
            )

    return wrapper
