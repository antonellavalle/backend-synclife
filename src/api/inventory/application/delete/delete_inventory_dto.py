from dataclasses import dataclass


@dataclass
class DeleteInventoryDTO:
    inventory_uuid: str
    session_token: str
