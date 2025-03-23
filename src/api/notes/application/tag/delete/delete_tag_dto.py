from dataclasses import dataclass


@dataclass
class DeleteTagDTO:
    tag_uuid: str
    session_token: str
