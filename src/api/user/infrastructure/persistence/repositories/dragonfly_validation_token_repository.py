"""
Module that implements the validation token repository using Dragonfly in the user
infrastructure layer.

This repository uses Redis to manage validation tokens associated with account
verification, allowing for the creation, lookup, and deletion of such tokens.
"""

from datetime import timedelta
from typing import Optional

import redis

from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_dragonfly_connection
from src.api.user.domain.repositories import ValidationTokenRepository


class DragonflyValidationTokenRepository(ValidationTokenRepository):
    """
    Validation token repository implemented with Dragonfly (Redis).

    This class implements the ValidationTokenRepository interface using Redis as the
    persistence system, enabling the management of validation token requests associated
    with users.

    Attributes:
        __client (redis.Redis): Redis client used to interact with the token database.
        __session_duration (timedelta): Duration for which the validation token remains
                                        valid.
    """

    def __init__(self, client: redis.Redis):
        """
        Initializes a new instance of DragonflyValidationTokenRepository.

        Args:
            client (redis.Redis): Redis client that will be used to manage validation
                                  tokens.
        """
        self.__client = client
        self.__session_duration = timedelta(hours=48)

    @staticmethod
    def get_repository() -> "DragonflyValidationTokenRepository":
        """
        Obtains an instance of the repository using a connection to Dragonfly (Redis).

        Returns:
            DragonflyValidationTokenRepository: An instance of the repository with the
                                                established connection.
        """
        return DragonflyValidationTokenRepository(get_dragonfly_connection())

    def create_validation_request(self, user_uuid: Uuid) -> str:
        """
        Creates a validation request by generating a token associated with the user's
        UUID.

        The token is stored in Redis with an expiration time defined by
        __session_duration.

        Args:
            user_uuid (Uuid): Unique identifier of the user for whom the validation
                              token is generated.

        Returns:
            str: The generated validation token.
        """
        validate_token = str(Uuid())
        self.__client.setex(
            validate_token, int(self.__session_duration.total_seconds()), str(user_uuid)
        )
        return validate_token

    def find_user_from_validation_request(self, validate_token: str) -> Optional[Uuid]:
        """
        Finds and returns the UUID of the user associated with a validation token.

        Args:
            validate_token (str): The validation token to query.

        Returns:
            Optional[Uuid]: The user's UUID associated with the token, or None if not
                            found.
        """
        user = self.__client.get(validate_token)
        return Uuid(str(user)) if user else None

    def delete_validation_request(self, validation_token: str) -> None:
        """
        Deletes a validation request based on the provided token.

        Args:
            validation_token (str): The validation token to be deleted from Redis.
        """
        self.__client.delete(validation_token)
