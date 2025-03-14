from dataclasses import dataclass
from datetime import date


@dataclass
class CreateItemDTO:
    product_name: str
    amount: int
    expiration_date: date
    session_token: str
