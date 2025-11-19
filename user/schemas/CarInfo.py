from pydantic import BaseModel

class Carinfo(BaseModel):
    brand: str
    model: str
    color: str
    year: int

class CarResponse(BaseModel):
    id: int
    brand: str
    model: str
    color: str
    year: int