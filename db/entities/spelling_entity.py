from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.orm import relationship

from db.data_context import Base

class spelling_entity(Base):
    __tablename__ = "SpellingGameEntry"
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, index=True)
    correctAnswer = Column(String(1), unique=False, index=False)
    wrongAnswer = Column(String(1), unique=False, index=False)