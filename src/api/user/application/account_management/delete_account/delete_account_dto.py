from dataclasses import dataclass


@dataclass
class DeleteAccountDTO:
    session_token: str
