from dataclasses import dataclass


@dataclass
class CreateTagDTO:
    user_id: str
    name: str
    session_token: str
