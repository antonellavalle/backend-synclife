from dataclasses import dataclass


@dataclass
class FilterNotesByTagDTO:
    tag_uuid: str
    session_token: str
