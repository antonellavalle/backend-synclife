from dataclasses import dataclass


@dataclass
class UpdateTagDTO:
    tag_id: str
    name: str
    session_token: str
