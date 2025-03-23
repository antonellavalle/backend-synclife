from dataclasses import dataclass


@dataclass
class UpdateTagDTO:
    tag_uuid: str
    name: str
    session_token: str
