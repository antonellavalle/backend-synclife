from dataclasses import dataclass


@dataclass
class CreateNoteDTO:
    title: str
    content: str
    session_token: str
