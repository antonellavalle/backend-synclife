"""
Initialization module for the user domain repositories.

This module imports and exposes the necessary interfaces for the persistence and
management of data related to the user, including the main repository (UserRepository)
and the token validation repository (ValidationTokenRepository). The __all__ attribute
is used to explicitly define the names that will be exported when this package is
imported.
"""

from .user_repository import UserRepository
from .validation_token_repository import ValidationTokenRepository

__all__ = ["UserRepository", "ValidationTokenRepository"]
