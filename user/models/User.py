from sqlalchemy import Column, Integer, String, Float
from database import Base
class User(Base):
    __tablename__ = "users"
    
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

    email = Column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False,
        index=True
    )

    color = Column(
        String(50),
        nullable=True,
    )

    weight = Column(
        Float,
        nullable=False,
        index=True
    )
    
    height = Column(
        Float,
        nullable=False, 
        index=True
    )