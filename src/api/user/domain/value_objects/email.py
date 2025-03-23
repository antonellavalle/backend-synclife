import re

from src.api.user.domain.errors.email_error import EmailError, EmailTypeError


class Email:
    __email: str

    def __init__(self, email: str) -> None:
        self.email = email

    def __repr__(self) -> str:
        return f"<Email({self.email})>"

    def __eq__(self, other: object) -> bool:
        return self.email == other.email if isinstance(other, Email) else False

    def __str__(self) -> str:
        return self.email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"  # noqa: E501
        if re.match(email_regex, value):
            self.__email = value
            return
        raise EmailError(error_type=EmailTypeError.INVALID_EMAIL)
