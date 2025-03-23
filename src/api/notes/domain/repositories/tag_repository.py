from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.notes.domain.entities.tag import Tag
from src.api.shared.domain.value_objects import Uuid


class TagRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Tag]:
        pass

    @abstractmethod
    def find_by_uuid(self, uuid: Uuid) -> Optional[Tag]:
        pass

    @abstractmethod
    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Tag]:
        pass

    @abstractmethod
    def find_by_name_and_user_uuid(self, name: str, user_uuid: Uuid) -> Optional[Tag]:
        pass

    @abstractmethod
    def save(self, tag: Tag) -> bool:
        pass

    @abstractmethod
    def delete(self, tag: Tag) -> Tuple[bool, Optional[Tag]]:
        pass

    @abstractmethod
    def update(self, tag: Tag) -> Tuple[bool, Optional[Tag]]:
        pass
