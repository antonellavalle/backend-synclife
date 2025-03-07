"""
Module that defines the DTO for account verification in the user application layer.

This DTO encapsulates the necessary information to verify a user's account using a
validation token.
"""

from dataclasses import dataclass


@dataclass
class VerifyAccountDTO:
    """
    Data Transfer Object for the user account verification use case.

    Attributes:
        validate_token (str): Validation token used to verify the user's account.
    """

    validate_token: str
