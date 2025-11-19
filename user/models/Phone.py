from sqlalchemy import Column, Integer, String
from database import Base

class Phone(Base):
    __tablename__ = "phones"

    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )

    name = Column(
        String(100),
        nullable=False ,
        index=True
    )

    color = Column(
        String(50),
        nullable=False
    )

    made_in = Column(
        String(100),
        nullable=False
    
    )
    waranty = Column(
        String(50),
        nullable=False
        )