from dataclasses import dataclass


@dataclass
class CreateNoteDTO:
    user_id: str
    title: str
    content: str
    session_token: str
