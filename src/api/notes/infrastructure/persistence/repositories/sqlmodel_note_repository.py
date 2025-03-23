from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.notes.domain.entities.note import Note
from src.api.notes.domain.repositories.note_repository import NoteRepository
from src.api.notes.infrastructure.persistence.models.sqlmodel_note_model import (
    SQLModelNoteModel,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_note_tag_link_model import (  # noqa: E501
    SQLModelNoteTagModel,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_tag_model import (
    SQLModelTagModel,
)
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.shared.infrastructure.persistence.sqlmodel_connection import (
    get_session as get_db_connection,
)


class SQLModelNoteRepository(NoteRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SQLModelNoteRepository":
        with get_db_connection() as db_connection:
            return SQLModelNoteRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Note]:
        query = (
            select(SQLModelNoteModel)
            if include_deleted
            else select(SQLModelNoteModel).where(not_(SQLModelNoteModel.is_deleted))
        )
        notes = self.db_connection.exec(query).all()
        return [note.to_entity() for note in notes]

    def find_by_uuid(self, uuid: Uuid, include_deleted: bool = False) -> Optional[Note]:
        query = (
            select(SQLModelNoteModel).where(SQLModelNoteModel.uuid == str(uuid))
            if include_deleted
            else (
                select(SQLModelNoteModel)
                .where(SQLModelNoteModel.uuid == str(uuid))
                .where(not_(SQLModelNoteModel.is_deleted))
            )
        )
        note = self.db_connection.exec(query).first()
        return note.to_entity() if note else None

    def find_by_tag(self, tag_uuid: Uuid, include_deleted: bool = False) -> List[Note]:
        query = (
            select(SQLModelNoteModel)
            .join(SQLModelNoteTagModel)
            .join(SQLModelTagModel)
            .where(SQLModelTagModel.uuid == str(tag_uuid))
            if include_deleted
            else (
                select(SQLModelNoteModel)
                .join(SQLModelNoteTagModel)
                .join(SQLModelTagModel)
                .where(SQLModelTagModel.uuid == str(tag_uuid))
                .where(not_(SQLModelNoteModel.is_deleted))
            )
        )
        notes = self.db_connection.exec(query).all()
        return [note.to_entity() for note in notes]

    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Note]:
        query = (
            select(SQLModelNoteModel).where(
                SQLModelNoteModel.user_uuid == str(user_uuid)
            )
            if include_deleted
            else select(SQLModelNoteModel)
            .where(SQLModelNoteModel.user_uuid == str(user_uuid))
            .where(not_(SQLModelNoteModel.is_deleted))
        )

        notes = self.db_connection.exec(query).all()
        return [note.to_entity() for note in notes]

    def find_by_title_and_user_uuid(
        self, title: str, user_uuid: Uuid, include_deleted: bool = False
    ) -> Optional[Note]:
        query = (
            select(SQLModelNoteModel)
            .where(SQLModelNoteModel.title == title)
            .where(SQLModelNoteModel.user_uuid == str(user_uuid))
            if include_deleted
            else (
                select(SQLModelNoteModel)
                .where(SQLModelNoteModel.title == title)
                .where(SQLModelNoteModel.user_uuid == str(user_uuid))
                .where(not_(SQLModelNoteModel.is_deleted))
            )
        )
        note = self.db_connection.exec(query).first()
        return note.to_entity() if note else None

    def save(self, note: Note) -> bool:
        note_model = SQLModelNoteModel.from_entity(note)

        # Sincronizar tags
        for tag in note.tags:
            tag_model = self.db_connection.exec(
                select(SQLModelTagModel).where(SQLModelTagModel.uuid == str(tag.uuid))
            ).first()
            if tag_model:
                note_model.tags.append(tag_model)

        self.db_connection.add(note_model)
        self.db_connection.commit()
        return True

    def update(self, note: Note) -> Tuple[bool, Optional[Note]]:
        existing_note = self.db_connection.exec(
            select(SQLModelNoteModel)
            .where(SQLModelNoteModel.uuid == str(note.uuid))
            .where(not_(SQLModelNoteModel.is_deleted))
        ).first()

        if not existing_note:
            return (False, None)

        # Actualizar campos de la nota
        updates = {
            "title": note.title,
            "content": note.content,
            "updated_at": datetime.now(),
        }
        for field, value in updates.items():
            if getattr(existing_note, field) != value:
                setattr(existing_note, field, value)

        # Sincronizar tags en la tabla intermedia
        existing_tags = {str(tag.uuid) for tag in existing_note.tags}
        new_tags = {str(tag.uuid) for tag in note.tags}

        # Agregar nuevas relaciones
        for tag_uuid in new_tags - existing_tags:
            tag = self.db_connection.exec(
                select(SQLModelTagModel).where(SQLModelTagModel.uuid == tag_uuid)
            ).first()
            if tag:
                existing_note.tags.append(tag)

        # Eliminar relaciones obsoletas
        for tag_uuid in existing_tags - new_tags:
            tag_to_remove = next(
                (tag for tag in existing_note.tags if tag.uuid == tag_uuid), None
            )
            if tag_to_remove:
                existing_note.tags.remove(tag_to_remove)

        self.db_connection.add(existing_note)
        self.db_connection.commit()
        self.db_connection.refresh(existing_note)

        return (True, existing_note.to_entity())

    def delete(self, note: Note) -> Tuple[bool, Optional[Note]]:
        existing_note = self.db_connection.exec(
            select(SQLModelNoteModel)
            .where(SQLModelNoteModel.uuid == str(note.uuid))
            .where(not_(SQLModelNoteModel.is_deleted))
        ).first()

        if not existing_note:
            return (False, None)

        existing_note.is_deleted = True
        existing_note.updated_at = datetime.now()
        self.db_connection.add(existing_note)
        self.db_connection.commit()
        self.db_connection.refresh(existing_note)

        return (True, existing_note.to_entity())
