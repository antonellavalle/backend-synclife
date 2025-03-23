from dataclasses import dataclass


@dataclass
class ViewTagDTO:
    tag_uuid: str
    session_token: str
