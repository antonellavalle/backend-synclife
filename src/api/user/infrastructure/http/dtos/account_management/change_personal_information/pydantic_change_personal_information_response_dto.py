from datetime import date

from pydantic import BaseModel, EmailStr


class PydanticChangePersonalInformationResponseDTO(BaseModel):
    email: EmailStr
    full_name: str
    birth_date: date
    phone: str
