from dataclasses import dataclass


@dataclass
class AccountRecoveryDTO:
    validate_token: str
