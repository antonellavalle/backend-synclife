"""
Module that defines the use case for account verification in the user application.

This module contains the VerifyAccountUseCase class, which implements the logic to
verify a user's account using a validation token. The process includes obtaining the
user's UUID from the token, verifying the account's status, updating it, and creating a
session for the user.
"""

from typing import Tuple

from src.api.shared.domain.repositories import SessionRepository
from src.api.user.application.authentication.verify_account.verify_account_dto import (
    VerifyAccountDTO,
)
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors import (
    UserRepositoryError,
    UserRepositoryTypeError,
    ValidateTokenRepositoryError,
    ValidateTokenRepositoryTypeError,
)
from src.api.user.domain.repositories import UserRepository, ValidationTokenRepository
from src.api.user.domain.validators import UserRepositoryValidator


class VerifyAccountUseCase:
    """
    Use case for verifying a user's account.

    This class implements the logic required to:
      1. Retrieve the user's UUID from the validation token.
      2. Validate that the user exists in the repository.
      3. Check that the account is not already verified.
      4. Update the user's account verification status.
      5. Persist the update and create a session for the verified user.

    Attributes:
        __user_repository (UserRepository): Repository for managing users.
        __validation_token_repository (ValidationTokenRepository): Repository for
                                                                   managing validation
                                                                   tokens.
        __session_repository (SessionRepository): Repository for creating and managing
                                                  sessions.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        validation_token_repository: ValidationTokenRepository,
        session_repository: SessionRepository,
    ) -> None:
        """
        Initializes a new instance of VerifyAccountUseCase.

        Args:
            user_repository (UserRepository): Repository for accessing user data.
            validation_token_repository (ValidationTokenRepository): Repository for
                                                                     managing validation
                                                                     tokens.
            session_repository (SessionRepository): Repository for creating and managing
                                                    sessions.
        """
        self.__user_repository = user_repository
        self.__validation_token_repository = validation_token_repository
        self.__session_repository = session_repository

    def execute(self, dto: VerifyAccountDTO) -> Tuple[User, str]:
        """
        Executes the use case to verify the user's account.

        Performs the following operations:
          1. Retrieves the UUID of the user associated with the provided validation
             token.
          2. If no user is found, raises an exception indicating that the token is
             invalid.
          3. Retrieves the user from the repository using the obtained UUID.
          4. If the user's account is already verified, raises an exception.
          5. Updates the user's account status to verified.
          6. Persists the update in the repository.
          7. Creates a session for the verified user.
          8. Returns a tuple containing the updated user and the generated session
             token.

        Args:
            dto (VerifyAccountDTO): Object containing the account validation token.

        Returns:
            Tuple[User, str]: A tuple with the verified User object and the created
                              session token.

        Raises:
            ValidateTokenRepositoryError: If the token is invalid or if the account is
                                          already verified.
            UserRepositoryError: If the user update operation fails.
        """
        user_uuid = (
            self.__validation_token_repository.find_user_from_validation_request(
                dto.validate_token
            )
        )

        if user_uuid is None:
            raise ValidateTokenRepositoryError(
                ValidateTokenRepositoryTypeError.INVALID_TOKEN
            )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(user_uuid)
        )

        if user.account_verified:
            raise ValidateTokenRepositoryError(
                ValidateTokenRepositoryTypeError.ALREADY_VERIFIED
            )

        user.account_verified = True

        is_updated, user_updated = self.__user_repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_updated, self.__session_repository.create_session(user_updated.uuid)
