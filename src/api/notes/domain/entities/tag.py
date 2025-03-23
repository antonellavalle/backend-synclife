from datetime import datetime
from typing import Optional

from src.api.notes.domain.errors.tag.tag_validation_error import (
    TagValidationError,
    TagValidationTypeError,
)
from src.api.shared.domain.value_objects import Uuid


class Tag:
    __uuid: Uuid
    __user_uuid: Uuid
    __name: str
    __is_deleted: bool
    __created_at: datetime
    __updated_at: Optional[datetime]

    def __init__(
        self,
        uuid: Uuid,
        user_uuid: Uuid,
        name: str,
        is_deleted: bool,
        created_at: datetime,
        updated_at: Optional[datetime],
    ):
        self.uuid = uuid
        self.user_uuid = user_uuid
        self.name = name
        self.is_deleted = is_deleted
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"<name=({self.name})>"

    def __str__(self) -> str:
        return f"Tag(Tag name: {self.name})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented
        return (
            self.uuid == other.uuid
            and self.user_uuid == other.user_uuid
            and self.name == other.name
            and self.is_deleted == other.is_deleted
            and self.created_at == other.created_at
            and self.updated_at == other.updated_at
        )

    @property
    def uuid(self) -> Uuid:
        return self.__uuid

    @uuid.setter
    def uuid(self, value: Uuid) -> None:
        self.__uuid = value

    @property
    def user_uuid(self) -> Uuid:
        return self.__user_uuid

    @user_uuid.setter
    def user_uuid(self, value: Uuid) -> None:
        self.__user_uuid = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise TagValidationError(error_type=TagValidationTypeError.INVALID_NAME)
        if len(value) > 200:
            raise TagValidationError(error_type=TagValidationTypeError.NAME_MAX)
        self.__name = value

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @created_at.setter
    def created_at(self, valor: datetime) -> None:
        self.__created_at = valor

    @property
    def updated_at(self) -> Optional[datetime]:
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, valor: Optional[datetime]) -> None:
        self.__updated_at = valor

    @property
    def is_deleted(self) -> bool:
        return self.__is_deleted

    @is_deleted.setter
    def is_deleted(self, valor: bool) -> None:
        self.__is_deleted = valor
