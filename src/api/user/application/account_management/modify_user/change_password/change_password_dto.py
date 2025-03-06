from dataclasses import dataclass


@dataclass
class ChangePasswordDto:
    validate_token: str
    new_password: str
