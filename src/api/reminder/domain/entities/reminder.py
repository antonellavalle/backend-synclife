from datetime import datetime
from typing import Optional

from src.api.reminder.domain.errors.reminder_validation_error import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.shared.domain.value_objects.uuid import Uuid


class Reminder:
    __uuid: Uuid
    __user_uuid: Uuid
    __title: str
    __remind_date: datetime
    __created_at: datetime
    __updated_at: Optional[datetime]
    __is_deleted: bool

    def __init__(
        self,
        uuid: Uuid,
        user_uuid: Uuid,
        title: str,
        remind_date: datetime,
        created_at: datetime,
        updated_at: Optional[datetime],
        is_deleted: bool,
    ):
        self.uuid = uuid
        self.user_uuid = user_uuid
        self.title = title
        self.remind_date = remind_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def __repr__(self) -> str:
        return (
            f"<Reminder(ID={self.uuid}, title={self.title}, "
            f"remind_date={self.remind_date})>"
            f"created_at={self.created_at})>"
        )

    def __str__(self) -> str:
        return (
            f"Title({self.title}, "
            f"Remind Date: {self.remind_date}, ID: {self.uuid}, "
            f"Created at={self.created_at}"
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
            raise ReminderValidationError(
                error_type=ReminderValidationTypeError.INVALID_TITLE
            )
        self.__title = value.strip()

    @property
    def remind_date(self) -> datetime:
        return self.__remind_date

    @remind_date.setter
    def remind_date(self, value: datetime) -> None:
        current_date = datetime.now()
        remind_date = value.replace(tzinfo=None)

        if remind_date < current_date:
            raise ReminderValidationError(
                error_type=ReminderValidationTypeError.INVALID_REMINDER_DATE
            )
        self.__remind_date = remind_date

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
