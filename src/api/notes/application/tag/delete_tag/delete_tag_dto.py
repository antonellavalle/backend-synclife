from dataclasses import dataclass


@dataclass
class DeleteTagDTO:
    tag_id: str
    session_token: str
