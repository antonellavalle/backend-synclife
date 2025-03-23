from src.api.shared.domain.errors.session_repository_error import (
    SessionRepositoryError,
    SessionRepositoryTypeError,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.value_objects.uuid import Uuid


class SessionRepositoryValidator:
    @staticmethod
    def validate_permission(user_request_uuid: Uuid, uuid: Uuid) -> None:
        if user_request_uuid != uuid:
            raise SessionRepositoryError(SessionRepositoryTypeError.INVALID_USER)

    # TODO: verificar si este metodo es async o no
    @staticmethod
    def validate_session_token(
        session_repository: SessionRepository, session_token: str
    ) -> str:
        user_uuid = session_repository.get_user_from_session(session_token)
        if not user_uuid:
            raise SessionRepositoryError(SessionRepositoryTypeError.INVALID_SESSION)
        return user_uuid
