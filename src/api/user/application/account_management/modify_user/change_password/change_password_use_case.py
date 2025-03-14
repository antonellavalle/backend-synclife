"""
Module that defines the use case for changing a user's password in the user application.

This module contains the ChangePasswordUseCase class, which implements the logic needed
to change an authenticated user's password using a validation token. The process
consists of:
  1. Obtaining the user's UUID from the validation token.
  2. Retrieving the user from the repository using the UUID.
  3. Updating the user's password with the new one provided.
  4. Persisting the update in the repository.
"""

from src.api.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDTO,
)
from src.api.user.domain.entities import User
from src.api.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.user.domain.errors.validate_token_repository_error import (
    ValidateTokenRepositoryError,
    ValidateTokenRepositoryTypeError,
)
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.repositories.validation_token_repository import (
    ValidationTokenRepository,
)
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects.password import Password


class ChangePasswordUseCase:
    """
    Use case for changing a user's password.

    This class implements the logic required to update a user's password. The process
    includes:
      - Obtaining the user's UUID from a validation token.
      - Retrieving the user from the repository using the UUID.
      - Updating the user's password with the new password provided.
      - Persisting the update in the repository and returning the updated user.

    Attributes:
        __user_repository (UserRepository): Repository for managing users.
        __validation_token_repository (ValidationTokenRepository): Repository for
                                                                   managing validation
                                                                   tokens.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        validation_token_repository: ValidationTokenRepository,
    ) -> None:
        """
        Initializes a new instance of ChangePasswordUseCase.

        Args:
            user_repository (UserRepository): User repository for accessing and
                                              modifying data.
            validation_token_repository (ValidationTokenRepository): Repository for
                                                                     creating and
                                                                     managing validation
                                                                     tokens.
        """
        self.__user_repository = user_repository
        self.__validation_token_repository = validation_token_repository

    def execute(self, dto: ChangePasswordDTO) -> User:
        """
        Executes the password change use case.

        Performs the following operations:
          1. Obtains the UUID of the user associated with the validation token provided
             in the DTO.
          2. If the UUID is not found, raises an exception indicating that the token is
             invalid.
          3. Retrieves the user from the repository using the obtained UUID.
          4. Updates the user's password with the new password provided in the DTO.
          5. Persists the update in the repository.
          6. Returns the updated user.

        Args:
            dto (ChangePasswordDTO): Object containing the validation token and the new
                                     password.

        Returns:
            User: The updated User object after the password change.

        Raises:
            ValidateTokenRepositoryError: If the validation token is invalid.
            UserRepositoryError: If the update operation fails.
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

        user.password = Password(dto.new_password)

        is_updated, user_updated = self.__user_repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_updated
