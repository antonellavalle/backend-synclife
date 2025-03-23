from dataclasses import dataclass


@dataclass
class UpdateNoteDTO:
    note_uuid: str
    title: str
    content: str
    session_token: str
