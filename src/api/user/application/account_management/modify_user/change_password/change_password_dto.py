from dataclasses import dataclass


@dataclass
class ChangePasswordDTO:
    validate_token: str
    new_password: str
