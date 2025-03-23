from dataclasses import dataclass


@dataclass
class RequestChangePasswordDTO:
    email: str
    url: str
