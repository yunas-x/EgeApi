import datetime
import hashlib
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date
from sqlalchemy.orm import relationship

from db.data_context import Base

class player_entity(Base):
    __tablename__ = "PlayerEntity"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    hashedPassword = Column(Integer, unique=False, index=False)
    registeredOn = Column(Date, unique=False, index=False, default=datetime.datetime.now())
    email = Column(String, unique=True, index=False)
    isActive = Column(Boolean, unique=False, index=False, default=True)
    
    games = relationship("score_entity", back_populates="player")

def hash_pass(string: str):
    return hashlib.md5(string.encode()).hexdigest()