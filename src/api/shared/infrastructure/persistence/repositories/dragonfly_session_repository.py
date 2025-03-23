from datetime import timedelta
from typing import Optional

import redis

from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.shared.infrastructure.persistence.dragonfly_connection import (
    get_dragonfly_connection,
)


class DragonflySessionRepository(SessionRepository):
    def __init__(self, client: redis.Redis):
        self.__client = client
        self.__session_duration = timedelta(hours=24)

    @staticmethod
    def get_repository() -> "DragonflySessionRepository":
        return DragonflySessionRepository(get_dragonfly_connection())

    def create_session(self, user_uuid: Uuid) -> str:
        session_token = str(Uuid())
        self.__client.setex(
            session_token, int(self.__session_duration.total_seconds()), str(user_uuid)
        )
        return session_token

    def get_user_from_session(self, session_token: str) -> Optional[str]:
        user = self.__client.get(session_token)
        if user is not None:
            return str(user)
        return None

    def delete_session(self, session_token: str) -> None:
        self.__client.delete(session_token)
