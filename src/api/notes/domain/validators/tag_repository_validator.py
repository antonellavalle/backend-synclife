from typing import Optional

from src.api.notes.domain.entities.tag import Tag
from src.api.notes.domain.errors.tag.tag_repository_error import (
    TagRepositoryError,
    TagRepositoryTypeError,
)
from src.api.notes.domain.repositories.tag_repository import TagRepository
from src.api.shared.domain.value_objects.uuid import Uuid


class TagRepositoryValidator:
    @staticmethod
    def tag_found(tag: Optional[Tag]) -> Tag:
        if tag is None:
            raise TagRepositoryError(error_type=TagRepositoryTypeError.NOT_FOUND)
        return tag

    @staticmethod
    def user_owns_tag(
        tag_repository: TagRepository, user_uuid: Uuid, tag_uuid: Uuid
    ) -> None:
        tag = tag_repository.find_by_uuid(uuid=tag_uuid)
        if tag is None or tag.user_uuid != user_uuid:
            raise TagRepositoryError(error_type=TagRepositoryTypeError.NOT_OWNED)

    @staticmethod
    def tag_name_unique(
        tag_repository: TagRepository, name: str, user_uuid: Uuid
    ) -> None:
        if tag_repository.find_by_name_and_user_uuid(name=name, user_uuid=user_uuid):
            raise TagRepositoryError(error_type=TagRepositoryTypeError.DUPLICATED_NAME)
