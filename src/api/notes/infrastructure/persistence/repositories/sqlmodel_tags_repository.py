from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.notes.domain.entities.tags import Tags
from src.api.notes.domain.repositories.tags_repository import TagsRepository
from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SQLModelTagsModel,
)
from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_db_connection


class SQLModelTagsRepository(TagsRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SQLModelTagsRepository":
        with get_db_connection() as db_connection:
            return SQLModelTagsRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Tags]:
        query = (
            select(SQLModelTagsModel)
            if include_deleted
            else select(SQLModelTagsModel).where(not_(SQLModelTagsModel.is_deleted))
        )
        tags = self.db_connection.exec(query).all()
        return [tag.to_entity() for tag in tags]

    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[Tags]:
        query = (
            select(SQLModelTagsModel).where(SQLModelTagsModel.id == str(id))
            if include_deleted
            else (
                select(SQLModelTagsModel)
                .where(SQLModelTagsModel.id == str(id))
                .where(not_(SQLModelTagsModel.is_deleted))
            )
        )
        tag = self.db_connection.exec(query).first()
        return tag.to_entity() if tag else None

    def find_all_by_user_id(
        self, user_id: Uuid, include_deleted: bool = False
    ) -> List[Tags]:
        query = select(SQLModelTagsModel).where(
            SQLModelTagsModel.user_id == str(user_id)
        )

        if not include_deleted:
            query = query.where(not_(SQLModelTagsModel.is_deleted))

        tags = self.db_connection.exec(query).all()
        return [tag.to_entity() for tag in tags]

    def find_by_name_and_user_id(self, name: str, user_id: Uuid) -> Optional[Tags]:
        query = (
            select(SQLModelTagsModel)
            .where(SQLModelTagsModel.name == name)
            .where(SQLModelTagsModel.user_id == str(user_id))
            .where(not_(SQLModelTagsModel.is_deleted))
        )
        tag = self.db_connection.exec(query).first()
        return tag.to_entity() if tag else None

    def save(self, tag: Tags) -> bool:
        tag_model = SQLModelTagsModel.from_entity(tag)
        self.db_connection.add(tag_model)
        self.db_connection.commit()
        return True

    def update(self, tag: Tags) -> Tuple[bool, Optional[Tags]]:
        existing_tag = self.db_connection.exec(
            select(SQLModelTagsModel)
            .where(SQLModelTagsModel.id == str(tag.id))
            .where(not_(SQLModelTagsModel.is_deleted))
        ).first()

        if not existing_tag:
            return (False, None)

        updates = {"name": tag.name, "updated_at": datetime.now()}
        for field, value in updates.items():
            if getattr(existing_tag, field) != value:
                setattr(existing_tag, field, value)

        self.db_connection.add(existing_tag)
        self.db_connection.commit()
        self.db_connection.refresh(existing_tag)

        return (True, existing_tag.to_entity())

    def delete(self, tag: Tags) -> Tuple[bool, Optional[Tags]]:
        existing_tag = self.db_connection.exec(
            select(SQLModelTagsModel)
            .where(SQLModelTagsModel.id == str(tag.id))
            .where(not_(SQLModelTagsModel.is_deleted))
        ).first()

        if not existing_tag:
            return (False, None)

        existing_tag.is_deleted = True
        existing_tag.updated_at = datetime.now()
        self.db_connection.add(existing_tag)
        self.db_connection.commit()
        self.db_connection.refresh(existing_tag)

        return (True, existing_tag.to_entity())
