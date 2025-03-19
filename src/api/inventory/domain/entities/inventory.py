from datetime import date, datetime
from typing import Optional

from src.api.inventory.domain.errors.inventory_validation_error import (
    InventoryValidationError,
    InventoryValidationTypeError,
)
from src.api.shared.domain.value_objects import Uuid


class Inventory:
    __uuid: Uuid
    __user_uuid: Uuid
    __product_name: str
    __amount: int
    __expiration_date: date
    __created_at: datetime
    __updated_at: Optional[datetime]
    __is_deleted: bool

    def __init__(
        self,
        uuid: Uuid,
        user_uuid: Uuid,
        product_name: str,
        amount: int,
        expiration_date: date,
        created_at: datetime,
        updated_at: Optional[datetime],
        is_deleted: bool,
    ):
        self.uuid = uuid
        self.user_uuid = user_uuid
        self.product_name = product_name
        self.amount = amount
        self.expiration_date = expiration_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def __repr__(self) -> str:
        return (
            f"<InventoryItem(uuid={self.uuid},"
            f"product_name={self.product_name},"
            f"amount={self.amount})>"
        )

    def __str__(self) -> str:
        return (
            f"InventoryItem(Product name: {self.product_name}, "
            f"Amount: {self.amount}, Expiration date: {self.expiration_date})"
        )

    @property
    def uuid(self) -> Uuid:
        return self.__uuid

    @uuid.setter
    def uuid(self, value: Uuid) -> None:
        self.__uuid = value

    @property
    def user_uuid(self) -> Uuid:
        return self.__user_uuid

    @user_uuid.setter
    def user_uuid(self, value: Uuid) -> None:
        self.__user_uuid = value

    @property
    def product_name(self) -> str:
        return self.__product_name

    @product_name.setter
    def product_name(self, value: str) -> None:
        if not value:
            raise InventoryValidationError(
                InventoryValidationTypeError.INVALID_PRODUCT_NAME
            )
        self.__product_name = value

    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, value: int) -> None:
        if value <= 0:
            raise InventoryValidationError(InventoryValidationTypeError.INVALID_AMOUNT)
        self.__amount = value

    @property
    def expiration_date(self) -> date:
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: date) -> None:
        if value < date.today():
            raise InventoryValidationError(InventoryValidationTypeError.EXPIRED_ITEM)
        self.__expiration_date = value

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @created_at.setter
    def created_at(self, valor: datetime) -> None:
        self.__created_at = valor

    @property
    def updated_at(self) -> Optional[datetime]:
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, valor: Optional[datetime]) -> None:
        self.__updated_at = valor

    @property
    def is_deleted(self) -> bool:
        return self.__is_deleted

    @is_deleted.setter
    def is_deleted(self, valor: bool) -> None:
        self.__is_deleted = valor
