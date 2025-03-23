from dataclasses import dataclass


@dataclass
class RequestAccountRecoveryDTO:
    email: str
    url: str
