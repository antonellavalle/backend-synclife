from datetime import datetime
from typing import List, Optional

from src.api.notes.domain.entities.tag import Tag
from src.api.notes.domain.errors.note.note_validation_error import (
    NoteValidationError,
    NoteValidationTypeError,
)
from src.api.shared.domain.value_objects import Uuid


class Note:
    __uuid: Uuid
    __user_uuid: Uuid
    __title: str
    __content: str
    __tags: List[Tag] = []
    __is_deleted: bool
    __created_at: datetime
    __updated_at: Optional[datetime]

    def __init__(
        self,
        uuid: Uuid,
        user_uuid: Uuid,
        title: str,
        content: str,
        tags: List[Tag],
        is_deleted: bool,
        created_at: datetime,
        updated_at: Optional[datetime],
    ):
        self.uuid = uuid
        self.user_uuid = user_uuid
        self.title = title
        self.content = content
        self.tags = tags
        self.is_deleted = is_deleted
        self.created_at = created_at
        self.updated_at = updated_at

    def add_tag(self, tag: Tag) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: Tag) -> None:
        if tag in self.tags:
            self.tags.remove(tag)

    def __repr__(self) -> str:
        return (
            f"<title(={self.title},"
            f"content={self.content},"
            f"created_at={self.created_at})>"
        )

    def __str__(self) -> str:
        return (
            f"Note(Note title: {self.title},"
            f"Content: {self.content},"
            f"Created at: {self.created_at})"
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        if not value:
            raise NoteValidationError(error_type=NoteValidationTypeError.INVALID_TITLE)
        if len(value) > 200:
            raise NoteValidationError(error_type=NoteValidationTypeError.TITLE_MAX)
        self.__title = value

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if not value.strip():
            raise NoteValidationError(
                error_type=NoteValidationTypeError.INVALID_CONTENT
            )
        if len(value) > 2500:
            raise NoteValidationError(error_type=NoteValidationTypeError.CONTENT_MAX)
        if len(value.split()) < 1:
            raise NoteValidationError(error_type=NoteValidationTypeError.CONTENT_MIN)
        self.__content = value

    @property
    def tags(self) -> List[Tag]:
        return self.__tags

    @tags.setter
    def tags(self, value: List[Tag]) -> None:
        self.__tags = value

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
