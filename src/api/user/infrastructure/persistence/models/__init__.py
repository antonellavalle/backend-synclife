"""
Initialization module for the persistence models in the user infrastructure layer.

This module imports and exposes the SQLModelUserModel, which is used to map the User
entity to the database. The __all__ attribute is used to explicitly define the names
that will be exported when importing this package.
"""

from .sqlmodel_user_model import SQLModelUserModel

__all__ = ["SQLModelUserModel"]
