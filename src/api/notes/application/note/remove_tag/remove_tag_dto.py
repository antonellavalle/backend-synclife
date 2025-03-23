from dataclasses import dataclass


@dataclass
class RemoveTagDTO:
    note_uuid: str
    tag_uuid: str
    session_token: str
