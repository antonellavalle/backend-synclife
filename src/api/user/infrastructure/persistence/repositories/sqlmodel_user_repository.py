"""
Module that implements the user repository using SQLModel in the infrastructure layer.

This repository allows performing CRUD operations on the User entity by interacting with
the database via SQLModel. It uses a connection obtained through get_db_connection to
execute queries.
"""

from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_db_connection
from src.api.user.domain.entities import User
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.value_objects import Email
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class SqlModelUserRepository(UserRepository):
    """
    User repository implemented with SQLModel.

    This class implements the UserRepository interface to manage users in the database.
    It provides methods to find, save, update, and delete users.

    Attributes:
        __db_connection (Session): Database connection used to execute operations.
    """

    def __init__(self, db_connection: Session) -> None:
        """
        Initializes a new instance of SqlModelUserRepository.

        Args:
            db_connection (Session): Database connection.
        """
        self.__db_connection = db_connection

    @staticmethod
    def get_repository() -> "SqlModelUserRepository":
        """
        Obtains an instance of the repository using a database connection.

        Uses the context manager from get_db_connection to obtain a connection and
        returns an instance of SqlModelUserRepository.

        Returns:
            SqlModelUserRepository: Instance of the repository with the established
                                    connection.
        """
        with get_db_connection() as db_connection:
            return SqlModelUserRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[User]:
        """
        Finds and returns all users.

        Args:
            include_deleted (bool, optional): Indicates whether to include users marked
                                              as deleted.
                                              Default is False.

        Returns:
            List[User]: List of found users, converted to domain entities.
        """
        query = (
            select(SqlModelUserModel)
            if include_deleted
            else select(SqlModelUserModel).where(not_(SqlModelUserModel.is_deleted))
        )
        users = self.__db_connection.exec(query).all()
        return [user.to_entity() for user in users]

    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[User]:
        """
        Finds a user by their unique identifier (UUID).

        Args:
            id (Uuid): Unique identifier of the user.
            include_deleted (bool, optional): Indicates whether to include deleted
                                              users.
                                              Default is False.

        Returns:
            Optional[User]: The User entity if found, or None otherwise.
        """
        query = (
            select(SqlModelUserModel).where(SqlModelUserModel.id == id)
            if include_deleted
            else (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.id == str(id))
                .where(not_(SqlModelUserModel.is_deleted))
            )
        )
        user = self.__db_connection.exec(query).first()
        return user.to_entity() if user else None

    def find_by_email(
        self, email: Email, include_deleted: bool = False, validate: bool = True
    ) -> Optional[User]:
        """
        Finds a user by their email address.

        Args:
            email (Email): Email address to search for.
            include_deleted (bool, optional): Indicates whether to include deleted
                                              users.
                                              Default is False.
            validate (bool, optional): Indicates whether the password should be
                                       validated when converting the entity.
                                       Default is True.

        Returns:
            Optional[User]: The found User entity or None if not found.
        """
        query = (
            select(SqlModelUserModel).where(SqlModelUserModel.email == str(email))
            if include_deleted
            else (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.email == str(email))
                .where(not_(SqlModelUserModel.is_deleted))
            )
        )
        user = self.__db_connection.exec(query).first()

        return user.to_entity(validate) if user else None

    def save(self, user: User) -> bool:
        """
        Saves a new user to the database.

        Args:
            user (User): The User entity to save.

        Returns:
            bool: True if the operation was successful.
        """
        user_model = SqlModelUserModel.from_entity(user)
        self.__db_connection.add(user_model)
        self.__db_connection.commit()
        return True

    def update(self, user: User) -> Tuple[bool, Optional[User]]:
        """
        Updates the information of an existing user.

        Searches for the user in the database, updates the fields that have changed,
        and persists the modifications.

        Args:
            user (User): The User entity with updated data.

        Returns:
            Tuple[bool, Optional[User]]: A tuple where the first element is True if the
                                         update was successful, and the second element
                                         is the updated User entity, or None if the user
                                         was not found.
        """
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == str(user.uuid)
        )
        db_user = self.__db_connection.exec(statement).first()

        if not db_user:
            return (False, None)

        updates = {
            "email": user.email.email,
            "password": user.password.password,
            "first_name": user.full_name.first_name,
            "last_name": user.full_name.last_name,
            "account_verified": user.account_verified,
            "birth_date": user.birth_date,
            "phone": user.phone.phone,
        }
        for field, value in updates.items():
            if getattr(db_user, field) != value:
                setattr(db_user, field, value)

        db_user.updated_at = datetime.now()
        self.__db_connection.add(db_user)
        self.__db_connection.commit()
        self.__db_connection.refresh(db_user)

        return (True, db_user.to_entity())

    def delete(self, user: User) -> Tuple[bool, Optional[User]]:
        """
        Marks a user as deleted in the database.

        Args:
            user (User): The User entity to delete.

        Returns:
            Tuple[bool, Optional[User]]: A tuple where the first element is True if the
                                         deletion was successful, and the second element
                                         is the deleted User entity, or None if the user
                                         was not found.
        """
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == user.uuid.uuid
        )
        db_user = self.__db_connection.exec(statement).first()

        if not db_user:
            return (False, None)

        db_user.is_deleted = True
        db_user.updated_at = datetime.now()
        self.__db_connection.add(db_user)
        self.__db_connection.commit()
        self.__db_connection.refresh(db_user)

        return (True, db_user.to_entity())
