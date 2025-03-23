from abc import ABC, abstractmethod
from typing import Optional

from src.api.shared.domain.value_objects.uuid import Uuid


class SessionRepository(ABC):
    @abstractmethod
    def create_session(self, user_uuid: Uuid) -> str:
        pass

    @abstractmethod
    def get_user_from_session(self, session_token: str) -> Optional[str]:
        pass

    @abstractmethod
    def delete_session(self, session_token: str) -> None:
        pass
