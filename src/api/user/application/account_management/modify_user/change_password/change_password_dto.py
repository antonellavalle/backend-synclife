"""
Module that defines the DTO for password change in the user application.

This DTO encapsulates the necessary information to change a user's password, including
the validation token and the new password.
"""

from dataclasses import dataclass


@dataclass
class ChangePasswordDto:
    """
    Data Transfer Object for changing a user's password.

    Attributes:
        validate_token (str): Validation token used to authorize the password change.
        new_password (str): The new password to be set.
    """

    validate_token: str
    new_password: str
