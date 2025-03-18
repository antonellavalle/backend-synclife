from datetime import date, datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.orm import Mapped
from sqlmodel import Field, Relationship, SQLModel

from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.entities.user import User
from src.api.user.domain.value_objects.email import Email
from src.api.user.domain.value_objects.full_name import FullName
from src.api.user.domain.value_objects.password import Password
from src.api.user.domain.value_objects.phone import Phone

if TYPE_CHECKING:
    from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
        SQLModelInventoryModel,
    )
    from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (  # noqa: E501
        SQLModelNotesModel,
    )
    from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
        SQLModelTagsModel,
    )
    from src.api.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (  # noqa: E501
        SQLModelReminderModel,
    )


class SQLModelUserModel(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
    account_verified: bool = Field(default=False)
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)

    inventory_items: Mapped[List["SQLModelInventoryModel"]] = Relationship(
        back_populates="user"
    )
    notes: Mapped[List["SQLModelNotesModel"]] = Relationship(back_populates="user")
    tags: Mapped[List["SQLModelTagsModel"]] = Relationship(back_populates="user")
    reminder_items: Mapped[List["SQLModelReminderModel"]] = Relationship(
        back_populates="user"
    )

    @classmethod
    def from_entity(cls, entity: User) -> "SQLModelUserModel":
        return cls(
            id=str(entity.uuid.uuid),
            email=entity.email.email,
            password=entity.password.password,
            first_name=entity.full_name.first_name,
            last_name=entity.full_name.last_name,
            birth_date=entity.birth_date,
            phone=entity.phone.phone,
            account_verified=entity.account_verified,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self, validate: bool = True) -> User:
        return User(
            uuid=Uuid(self.id),
            email=Email(self.email),
            password=Password(self.password, validate),
            full_name=FullName(self.first_name, self.last_name),
            birth_date=self.birth_date,
            phone=Phone(self.phone),
            account_verified=self.account_verified,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
