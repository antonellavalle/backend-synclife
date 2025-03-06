from dataclasses import dataclass


@dataclass
class RequestChangePasswordDto:
    email: str
    url: str
