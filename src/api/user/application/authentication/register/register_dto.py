"""
Module that defines the DTO for user registration in the application layer.

This DTO encapsulates the necessary data to register a user in the system, including
email, password, first name, last name, birth date, phone, and an associated URL (e.g.,
for verification or reference).
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class RegisterDTO:
    """
    Data Transfer Object for user registration.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        birth_date (date): The user's birth date.
        phone (str): The user's phone number.
        url (str): An associated URL for the user, used for verification or reference.
    """

    email: str
    password: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
    url: str
