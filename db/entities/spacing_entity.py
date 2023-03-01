from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.orm import relationship

from db.data_context import Base

class spacing_entity(Base):
    __tablename__ = "SpacingGameEntry"
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, index=True)
    correctAnswer = Column(Integer, unique=False, index=False)