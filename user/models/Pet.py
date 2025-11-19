from sqlalchemy import Column, Integer, String
from database import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )

    name = Column(
        String(100),
        nullable=False, 
        index=True
    )
    
    age = Column(
        Integer, 
        nullable=False,
        index=True
    )

    color = Column(
        String(50),
        nullable=False, 
        index=True
    )