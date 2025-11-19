from pydantic import BaseModel

class PetInfo(BaseModel):
    name: str
    age: int
    color: str

class PetResponse(BaseModel):
    id: int
    name: str
    age: int
    color: str