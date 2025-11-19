from pydantic import BaseModel

class PhoneInfo(BaseModel):
    name: str
    color: str
    made_in: str
    waranty: int

class PhoneResponse(BaseModel):
    id: int
    name: str
    color: str
    made_in: str
    waranty: int