from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.notes.domain.entities.note import Note
from src.api.shared.domain.value_objects import Uuid


class NoteRepository(ABC):
    @abstractmethod
    def find_all(self, include_deleted: bool = False) -> List[Note]:
        pass

    @abstractmethod
    def find_by_uuid(self, uuid: Uuid, include_deleted: bool = False) -> Optional[Note]:
        pass

    @abstractmethod
    def find_by_tag(self, tag_uuid: Uuid, include_deleted: bool = False) -> List[Note]:
        pass

    @abstractmethod
    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Note]:
        pass

    @abstractmethod
    def find_by_title_and_user_uuid(
        self, title: str, user_uuid: Uuid, include_deleted: bool = False
    ) -> Optional[Note]:
        pass

    @abstractmethod
    def save(self, note: Note) -> bool:
        pass

    @abstractmethod
    def delete(self, note: Note) -> Tuple[bool, Optional[Note]]:
        pass

    @abstractmethod
    def update(self, note: Note) -> Tuple[bool, Optional[Note]]:
        pass
