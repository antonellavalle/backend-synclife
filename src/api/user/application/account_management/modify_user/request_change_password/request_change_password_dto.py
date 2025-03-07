"""
Module that defines the DTO for requesting a password change in the user application.

This DTO encapsulates the necessary data to initiate the password change process,
including the user's email address and an associated URL to complete the action.
"""

from dataclasses import dataclass


@dataclass
class RequestChangePasswordDto:
    """
    Data Transfer Object for requesting a user's password change.

    Attributes:
        email (str): The user's email address.
        url (str): The URL that will be used to complete the password change process.
    """

    email: str
    url: str
