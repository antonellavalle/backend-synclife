"""
Module that defines the interface for the token validation repository in the user
domain.

This module contains the abstract class ValidationTokenRepository, which specifies the
necessary methods to manage token validation requests, used in processes such as user
account verification.
"""

from abc import ABC, abstractmethod
from typing import Optional

from src.api.shared.domain.value_objects import Uuid


class ValidationTokenRepository(ABC):
    """
    Abstract interface for the user token validation repository.

    This class defines the necessary methods to:
      - Create a token validation request associated with a user's UUID.
      - Find the UUID of a user based on a validation token.
      - Delete a validation request using the corresponding token.

    These methods must be implemented by a concrete class that interacts with the
    persistence system.
    """

    @abstractmethod
    def create_validation_request(self, user_uuid: Uuid) -> str:
        """
        Creates a token validation request for the specified user.

        Generates and returns a validation token associated with the user's UUID, which
        will be used for verification processes, such as account confirmation.

        Args:
            user_uuid (Uuid): The unique identifier of the user for whom the validation
                              token is generated.

        Returns:
            str: The generated validation token.
        """
        pass

    @abstractmethod
    def find_user_from_validation_request(self, validate_token: str) -> Optional[Uuid]:
        """
        Finds and returns the UUID of the user associated with a validation token.

        Queries the repository to find the identifier of the user related to the
        provided validation token.
        If no request is found, None is returned.

        Args:
            validate_token (str): The validation token to query.

        Returns:
            Optional[Uuid]: The UUID of the user associated with the token, or None if
                            not found.
        """
        pass

    @abstractmethod
    def delete_validation_request(self, validation_token: str) -> None:
        """
        Deletes the token validation request.

        Removes from the repository the validation request associated with the provided
        token, typically once the verification process is completed or when the request
        needs to be canceled.

        Args:
            validation_token (str): The validation token to delete.

        Returns:
            None
        """
        pass
