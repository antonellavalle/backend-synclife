from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.notes.domain.entities.tag import Tag
from src.api.notes.domain.repositories.tag_repository import TagRepository
from src.api.notes.infrastructure.persistence.models.sqlmodel_tag_model import (
    SQLModelTagModel,
)
from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_db_connection


class SQLModelTagRepository(TagRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SQLModelTagRepository":
        with get_db_connection() as db_connection:
            return SQLModelTagRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Tag]:
        query = (
            select(SQLModelTagModel)
            if include_deleted
            else select(SQLModelTagModel).where(not_(SQLModelTagModel.is_deleted))
        )
        tags = self.db_connection.exec(query).all()
        return [tag.to_entity() for tag in tags]

    def find_by_uuid(self, uuid: Uuid, include_deleted: bool = False) -> Optional[Tag]:
        query = (
            select(SQLModelTagModel).where(SQLModelTagModel.uuid == str(uuid))
            if include_deleted
            else (
                select(SQLModelTagModel)
                .where(SQLModelTagModel.uuid == str(uuid))
                .where(not_(SQLModelTagModel.is_deleted))
            )
        )
        tag = self.db_connection.exec(query).first()
        return tag.to_entity() if tag else None

    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Tag]:
        query = select(SQLModelTagModel).where(
            SQLModelTagModel.user_uuid == str(user_uuid)
        )

        if not include_deleted:
            query = query.where(not_(SQLModelTagModel.is_deleted))

        tags = self.db_connection.exec(query).all()
        return [tag.to_entity() for tag in tags]

    def find_by_name_and_user_uuid(self, name: str, user_uuid: Uuid) -> Optional[Tag]:
        query = (
            select(SQLModelTagModel)
            .where(SQLModelTagModel.name == name)
            .where(SQLModelTagModel.user_uuid == str(user_uuid))
            .where(not_(SQLModelTagModel.is_deleted))
        )
        tag = self.db_connection.exec(query).first()
        return tag.to_entity() if tag else None

    def save(self, tag: Tag) -> bool:
        tag_model = SQLModelTagModel.from_entity(tag)
        self.db_connection.add(tag_model)
        self.db_connection.commit()
        return True

    def update(self, tag: Tag) -> Tuple[bool, Optional[Tag]]:
        existing_tag = self.db_connection.exec(
            select(SQLModelTagModel)
            .where(SQLModelTagModel.uuid == str(tag.uuid))
            .where(not_(SQLModelTagModel.is_deleted))
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

    def delete(self, tag: Tag) -> Tuple[bool, Optional[Tag]]:
        existing_tag = self.db_connection.exec(
            select(SQLModelTagModel)
            .where(SQLModelTagModel.uuid == str(tag.uuid))
            .where(not_(SQLModelTagModel.is_deleted))
        ).first()

        if not existing_tag:
            return (False, None)

        existing_tag.is_deleted = True
        existing_tag.updated_at = datetime.now()
        self.db_connection.add(existing_tag)
        self.db_connection.commit()
        self.db_connection.refresh(existing_tag)

        return (True, existing_tag.to_entity())
