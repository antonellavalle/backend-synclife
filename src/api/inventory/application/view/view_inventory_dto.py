from dataclasses import dataclass


@dataclass
class ViewInventoryDTO:
    inventory_uuid: str
    session_token: str
