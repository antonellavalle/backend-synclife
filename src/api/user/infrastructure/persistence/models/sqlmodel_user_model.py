"""
Module that defines the SQLModel for the User entity in the infrastructure layer.

This model is used to map the User entity to the database schema, allowing the
persistence of user data. It also includes methods to transform a domain entity into
this model and vice versa.
"""

from datetime import date, datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.orm import Mapped
from sqlmodel import Field, Relationship, SQLModel

from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.entities import User
from src.api.user.domain.value_objects import Email, FullName, Password, Phone

if TYPE_CHECKING:
    from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
        SqlModelInventoryModel,
    )
    from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (  # noqa: E501
        SqlModelNotesModel,
    )
    from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
        SqlModelTagsModel,
    )
    from src.api.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (  # noqa: E501
        SqlModelReminderModel,
    )


class SqlModelUserModel(SQLModel, table=True):
    """
    SQLModel for the User entity.

    This model represents the "users" table in the database and maps the attributes of
    the User entity, allowing its persistence and retrieval. It also defines
    relationships with other entities such as inventory, notes, tags, and reminders.

    Attributes:
        id (str): Unique identifier of the user (primary key).
        email (str): User's email address (unique and indexed).
        password (str): User's encrypted password.
        first_name (str): User's first name.
        last_name (str): User's last name.
        birth_date (date): User's date of birth.
        phone (str): User's phone number.
        account_verified (bool): Indicates whether the user's account has been verified.
        is_deleted (bool): Indicates whether the user's account has been deleted.
        created_at (datetime): Date and time when the record was created.
        updated_at (Optional[datetime]): Date and time of the last update to the record.
        inventory_items (List[SqlModelInventoryModel]): Relationship with inventory
                                                        items associated with the user.
        notes (List[SqlModelNotesModel]): Relationship with notes associated with the
                                          user.
        tags (List[SqlModelTagsModel]): Relationship with tags associated with the user.
        reminder_items (List[SqlModelReminderModel]): Relationship with reminders
                                                      associated with the user.
    """

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

    inventory_items: Mapped[List["SqlModelInventoryModel"]] = Relationship(
        back_populates="user"
    )
    notes: Mapped[List["SqlModelNotesModel"]] = Relationship(back_populates="user")
    tags: Mapped[List["SqlModelTagsModel"]] = Relationship(back_populates="user")
    reminder_items: Mapped[List["SqlModelReminderModel"]] = Relationship(
        back_populates="user"
    )

    @classmethod
    def from_entity(cls, entity: User) -> "SqlModelUserModel":
        """
        Creates an instance of SqlModelUserModel from a User domain entity.

        Converts a User domain entity into its persistence representation in the
        database.

        Args:
            entity (User): The User domain entity.

        Returns:
            SqlModelUserModel: An instance of the SQLModel mapped with the entity's
                               data.
        """
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
        """
        Converts the SQLModel into a User domain entity.

        Transforms the instance of the model (persisted in the database) into the User
        domain entity, using the corresponding value objects and optionally validating
        the password.

        Args:
            validate (bool, optional): Indicates whether the password should be
                                       validated when creating the value object.
                                       Defaults to True.

        Returns:
            User: The User domain entity corresponding to the record.
        """
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
