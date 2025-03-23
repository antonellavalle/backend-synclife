from dataclasses import dataclass


@dataclass
class DeleteNoteDTO:
    note_uuid: str
    session_token: str
