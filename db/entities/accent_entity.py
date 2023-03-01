from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.data_context import Base

class accent_entity(Base):
    __tablename__ = "AccentGameEntry"
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, index=True)
    correctAnswer = Column(Integer, unique=False, index=False)