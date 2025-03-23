from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.reminder.domain.entities.reminder import Reminder
from src.api.reminder.domain.repositories.reminder_repository import ReminderRepository
from src.api.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (
    SQLModelReminderModel,
)
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.shared.infrastructure.persistence.sqlmodel_connection import (
    get_session as get_db_connection,
)


class SQLModelReminderRepository(ReminderRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SQLModelReminderRepository":
        with get_db_connection() as db_connection:
            return SQLModelReminderRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Reminder]:
        query = (
            select(SQLModelReminderModel)
            if include_deleted
            else select(SQLModelReminderModel).where(
                not_(SQLModelReminderModel.is_deleted)
            )
        )
        reminders = self.db_connection.exec(query).all()
        return [reminder.to_entity() for reminder in reminders]

    def find_by_uuid(
        self, uuid: Uuid, include_deleted: bool = False
    ) -> Optional[Reminder]:
        query = (
            select(SQLModelReminderModel).where(SQLModelReminderModel.uuid == str(uuid))
            if include_deleted
            else (
                select(SQLModelReminderModel)
                .where(SQLModelReminderModel.uuid == str(uuid))
                .where(not_(SQLModelReminderModel.is_deleted))
            )
        )
        reminder = self.db_connection.exec(query).first()
        return reminder.to_entity() if reminder else None

    def find_all_by_user_uuid(
        self, user_uuid: Uuid, include_deleted: bool = False
    ) -> List[Reminder]:
        query = select(SQLModelReminderModel).where(
            SQLModelReminderModel.user_uuid == str(user_uuid)
        )

        if not include_deleted:
            query = query.where(not_(SQLModelReminderModel.is_deleted))

        reminders = self.db_connection.exec(query).all()
        return [reminder.to_entity() for reminder in reminders]

    def save(self, reminder: Reminder) -> bool:
        reminder_model = SQLModelReminderModel.from_entity(reminder)
        self.db_connection.add(reminder_model)
        self.db_connection.commit()
        return True

    def update(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        existing_reminder = self.db_connection.exec(
            select(SQLModelReminderModel)
            .where(SQLModelReminderModel.uuid == str(reminder.uuid))
            .where(not_(SQLModelReminderModel.is_deleted))
        ).first()

        if not existing_reminder:
            return (False, None)

        updates = {
            "title": reminder.title,
            "remind_date": reminder.remind_date,
            "updated_at": datetime.now(),
        }
        for field, value in updates.items():
            if getattr(existing_reminder, field) != value:
                setattr(existing_reminder, field, value)

        self.db_connection.add(existing_reminder)
        self.db_connection.commit()
        self.db_connection.refresh(existing_reminder)

        result = (True, existing_reminder.to_entity())
        print(f"update() result: {result}")  # Imprime el resultado antes de devolverlo
        return result

    def delete(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        existing_reminder = self.db_connection.exec(
            select(SQLModelReminderModel)
            .where(SQLModelReminderModel.uuid == str(reminder.uuid))
            .where(not_(SQLModelReminderModel.is_deleted))
        ).first()

        if not existing_reminder:
            return (False, None)

        existing_reminder.is_deleted = True
        existing_reminder.updated_at = datetime.now()
        self.db_connection.add(existing_reminder)
        self.db_connection.commit()
        self.db_connection.refresh(existing_reminder)

        return (True, existing_reminder.to_entity())
