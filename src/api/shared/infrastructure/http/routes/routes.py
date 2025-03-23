from typing import Any

from fastapi import APIRouter, Header, HTTPException

from src.api.inventory.infrastructure.http.routes.fastapi_inventory_routes import (
    router as inventory_router,
)
from src.api.notes.infrastructure.http.routes.fastapi_note_routes import (
    router as note_router,
)
from src.api.notes.infrastructure.http.routes.fastapi_tag_routes import (
    router as tag_router,
)
from src.api.reminder.infrastructure.http.routes.fastapi_reminder_routes import (
    router as reminder_router,
)
from src.api.shared.infrastructure.persistence.repositories import (
    DragonflySessionRepository,
)
from src.api.user.infrastructure.http.routes.fastapi_user_routes import (
    router as user_router,
)

router: APIRouter = APIRouter()

router.include_router(user_router)
router.include_router(inventory_router)
router.include_router(note_router)
router.include_router(tag_router)
router.include_router(reminder_router)


@router.get("/check/validate-session", summary="Valida si la sesión es válida")
async def validate_session(session_token: str = Header(...)) -> dict[str, Any]:
    """
    Endpoint para validar si una sesión es válida.
    """
    session_repository = DragonflySessionRepository.get_repository()
    user_id = session_repository.get_user_from_session(session_token)

    if not user_id:
        raise HTTPException(status_code=401, detail="Sesión inválida o expirada")
    return {"valid": True, "user_id": user_id}
