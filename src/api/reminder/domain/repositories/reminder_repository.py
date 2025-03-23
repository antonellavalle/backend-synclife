from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.reminder.domain.entities.reminder import Reminder
from src.api.shared.domain.value_objects.uuid import Uuid


class ReminderRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Reminder]:
        pass

    @abstractmethod
    def find_by_uuid(
        self, uuid: Uuid, include_deleted: bool = False
    ) -> Optional[Reminder]:
        pass

    @abstractmethod
    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Reminder]:
        pass

    @abstractmethod
    def save(self, reminder: Reminder) -> bool:
        pass

    @abstractmethod
    def delete(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        pass

    @abstractmethod
    def update(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        pass
