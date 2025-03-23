from dataclasses import dataclass


@dataclass
class ViewNoteDTO:
    note_uuid: str
    session_token: str
